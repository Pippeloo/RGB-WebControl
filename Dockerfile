# syntax=docker/dockerfile:1
FROM arm32v7/python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD UDPsocket/UDP_Server_4CH.py /

#RUN apt-get update && apt-get install python3-pip -y
#RUN export CFLAGS=-fcommon
RUN apt-get install gcc python-dev
RUN python3-m pip install RPi.GPIO -y

RUN python3 -m pip install rpi_ws281x adafruit-circuitpython-neopixel
RUN python3 -m pip install --force-reinstall adafruit-blinka

CMD [ "python3", "UDP_Server_4CH.py" ]


