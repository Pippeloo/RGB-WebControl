# install the following libraries with pip
# sudo pip install rpi_ws281x adafruit-circuitpython-neopixel
# sudo python3 -m pip install --force-reinstall adafruit-blinka

import board
import neopixel
import socket
import json


host_name = socket.gethostname()
host_addr = socket.gethostbyname(host_name + ".local")

UDP_IP = host_addr
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message: ", data.decode("utf-8"))

    msg = json.loads(data.decode('ascii'))

    if ("p" in msg) and ("ch" in msg):
        if msg['ch'] == 1:
            pixels_1 = neopixel.NeoPixel(board.D18, msg['p'])
            print("Configurated Channel 1!")
        elif msg['ch'] == 2:
            pixels_2 = neopixel.NeoPixel(board.D21, msg['p'])
            print("Configurated Channel 2!")
        elif msg['ch'] == 3:
            pixels_3 = neopixel.NeoPixel(board.D12, msg['p'])
            print("Configurated Channel 3!")
        elif msg['ch'] == 4:
            pixels_4 = neopixel.NeoPixel(board.D10, msg['p'])
            print("Configurated Channel 4!")

    if "ch" in msg:
        if msg['ch'] == 1:
            if ("r" in msg) and ("g" in msg) and ("b" in msg):
                pixels_1.fill((msg['r'], msg['g'], msg['b']))
        elif msg['ch'] == 2:
            if ("r" in msg) and ("g" in msg) and ("b" in msg):
                pixels_2.fill((msg['r'], msg['g'], msg['b']))
                print(msg)
        elif msg['ch'] == 3:
            if ("r" in msg) and ("g" in msg) and ("b" in msg):
                pixels_3.fill((msg['r'], msg['g'], msg['b']))
        elif msg['ch'] == 4:
            if ("r" in msg) and ("g" in msg) and ("b" in msg):
                pixels_4.fill((msg['r'], msg['g'], msg['b']))
