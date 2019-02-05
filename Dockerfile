FROM python:3.7-alpine

COPY requirements.txt .

RUN apk add --no-cache bash py2-pip \
	&& pip3 install --upgrade pip \
	&& pip3 install --user -r requirements.txt

COPY app/ app

EXPOSE 5000

ENTRYPOINT ["python3", "app/run.py"]