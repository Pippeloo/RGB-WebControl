import board
import neopixel
import socket
import json


UDP_IP = '0.0.0.0'
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

debug = False

while True:
    data, addr = sock.recvfrom(1024)
    try:
        msg = json.loads(data.decode('ascii'))

        if ("debug" in msg):
            if (msg["debug"] == True):
                debug = True
                # return a message that debug is on
                sock.sendto(b"Debug is on", addr)
            else:
                debug = False
                # return a message that debug is off
                sock.sendto(b"Debug is Disabled", addr)

        if (debug == True):
            sock.sendto(b"RECEIVED: " + data, addr)

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

    except Exception as e:
        # send e to the client
        sock.sendto(b"Error: " + str(e), addr)
