import socket


def main():
    blacklist = ['']
    port = 3333  # Reserve a port for your service.
    s = socket.socket()  # Create a socket object
    s.bind(('', port))  # Bind to the port
    s.listen(5)

    # def sent(mes):
    #     port = 2222
    #     for i in ip:
    #         sock = socket.socket()
    #         sock.connect((i, port))
    #         print("Sent to ", ip, ":", port)
    #         mes_enc = mes.encode()
    #         sock.send(mes_enc)
    #         sock.close()


    # def customcmds(data):
    #     if data == "b'whosin'":
    #         print(addrbook)
    #     else:
    #         return False

    def newclient(conn, addr):
        data = conn.recv(1024)
        print("From ", addr[0], ": ", repr(data))

    while True:
        conn, addr = s.accept()
        newclient(conn, addr)
    s.close()


if __name__ == "__main__":
    main()
