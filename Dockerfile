# syntax=docker/dockerfile:1
FROM python:3

ADD UDPsocket/UDP_Server_4CH.py /

RUN python3 -m pip install RPi.GPIO
RUN python3 -m pip install rpi_ws281x adafruit-circuitpython-neopixel
RUN python3 -m pip install --force-reinstall adafruit-blinka

CMD [ "python3", "UDP_Server_4CH.py" ]


