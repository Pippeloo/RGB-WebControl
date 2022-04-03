FROM arm64v8/python:latest

COPY ./UDPsocket/UDP_Server_4CH.py ./

RUN pip install --no-cache-dir rpi.gpio
RUN pip install rpi_ws281x adafruit-circuitpython-neopixel

CMD ["python", "UDP_Server_4CH.py"]