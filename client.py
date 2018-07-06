import socket



def sent():
    mes = input(": ")
    port = 9999
    ip = "192.168.1.106"
    sock = socket.socket()
    sock.connect((ip, port))
    mes_enc = mes.encode()
    sock.send(mes_enc)
    sock.close()



message = " "
file = open('text.txt', 'w')

while message != "exit":
    sent()








