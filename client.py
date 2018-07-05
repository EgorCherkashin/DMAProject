import socket



def sent():
    mes = input(": ")
    port = 4444
    ip = "127.0.0.1"
    sock = socket.socket()
    sock.connect((ip, port))
    mes_enc = mes.encode()
    sock.send(mes_enc)
    sock.close()



message = " "
file = open('text.txt', 'w')

while message != "exit":
    sent()








