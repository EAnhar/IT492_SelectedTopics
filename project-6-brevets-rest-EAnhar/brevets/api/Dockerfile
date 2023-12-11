FROM python:3.9

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN mkdir /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["python3", "api.py"]



