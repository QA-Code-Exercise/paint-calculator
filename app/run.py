from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dimensions', methods=['GET'])
def dimensions():
    rooms = sanitize_input(request.args.get("rooms"))
    return render_template("dimensions.html", rooms=rooms)


@app.route('/results', methods=['POST'])
def results():
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

    all_data
    return render_template("results.html", all_data=all_data, total_gallons_required=total_gallons_required)


def calculate_feet(formatted_data):
    return int(formatted_data['length']) * int(formatted_data['width']) * int(formatted_data['height'])


def calculate_gallons_required(formatted_data):
    return math.ceil(formatted_data['ft'] / 400)


def sanitize_input(input):
    return abs(int(input))


def extract_room_info(data, room_number):
    formatted_data = {'length': sanitize_input(data.get("length-%d" % room_number)),
                      'width': sanitize_input(data.get("width-%d" % room_number)),
                      'height': sanitize_input(data.get("height-%d" % room_number))
                      }
    return formatted_data


if __name__ == '__main__':
    app.run()
