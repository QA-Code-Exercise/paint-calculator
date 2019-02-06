from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    """
    Loads the index page
    :return: Index page
    """
    return render_template("index.html")


@app.route('/dimensions', methods=['GET'])
def dimensions():
    """
    Sanitizes inputs from the first page and displays the Dimensions page
    :return: Dimensions page
    """
    rooms = sanitize_input(request.args.get("rooms"))
    return render_template("dimensions.html", rooms=rooms)


@app.route('/results', methods=['POST'])
def results():
    """
    Performs most of the logic for paint calculations
    :return: Results page
    """
    data = request.values
    number_of_data_sets = len(data) / 3
    all_data = []
    total_gallons_required = 0

    for room_number in range(int(number_of_data_sets)):
        formatted_data = extract_room_info(data, room_number)
        formatted_data['ft'] = calculate_feet(formatted_data)
        formatted_data['gallons'] = calculate_gallons_required(formatted_data)
        formatted_data['room'] = room_number + 1
        total_gallons_required += calculate_gallons_required(formatted_data)
        all_data.append(formatted_data)

    return render_template("results.html", all_data=all_data, total_gallons_required=total_gallons_required)


def calculate_feet(formatted_data):
    """
    Calculate the number of feet required to paint the surface area of a single room
    :param formatted_data: dict of L/W/H information
    :return: integer for the number of feet required by performing `((Length * 2) + (Width * 2)) * Height`
    """
    return int(formatted_data['length']) * int(formatted_data['width']) * int(formatted_data['height'])


def calculate_gallons_required(formatted_data):
    """
    Number of feet to paint divided by the amount of feet the paint will cover, rounded up
    :param formatted_data: An integer for the number of feet required to paint
    :return: feet / paint coverage, rounded up
    """
    return math.floor(formatted_data['ft'] / 350)


def sanitize_input(input):
    """
    This universe doesn't allow for negative numbers of rooms or feet
    :param input: Any number
    :return: The absolute, integer number
    """
    return abs(int(input))


def extract_room_info(data, room_number):
    """
    Sanitizes inputs, and then constructs a dict of the room information
    :param data: User input for LWH of a room
    :param room_number: The number of the room that is being processed
    :return: A formatted dict with room information
    """
    formatted_data = {'length': sanitize_input(data.get("length-%d" % room_number)),
                      'width': sanitize_input(data.get("width-%d" % room_number)),
                      'height': sanitize_input(data.get("height-%d" % room_number))
                      }
    return formatted_data


# Boiler plate for starting the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
