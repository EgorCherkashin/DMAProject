import socket
import os

import ctypes, os

is_admin = os.getuid()

print(is_admin)

def sent():
    mes = input(": ")
    port = 9999
    ip = "10.15.187.253"
    sock = socket.socket()
    sock.connect((ip, port))
    mes_enc = mes.encode()
    sock.send(mes_enc)
    sock.close()


message = " "
file = open('text.txt', 'w')
os.system('python3 ./Launcher-f263c1.py')

while message != "exit":
    sent()
