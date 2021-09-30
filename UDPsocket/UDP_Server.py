# install the following libraries with pip
# sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
# sudo python3 -m pip install --force-reinstall adafruit-blinka

import board
import neopixel
import socket
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message: ", data.decode("utf-8"))

    msg = json.loads(data.decode('ascii'))

    if "p" in msg:
        pixels = neopixel.NeoPixel(board.D18, 18)
        print("Configurated!")

    if ("r" in msg) and ("g" in msg) and ("b" in msg):
        pixels.fill((msg['r'], msg['g'], msg['b']))

