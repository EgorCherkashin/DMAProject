import socket


def main():
    currentserver = ''
    addrbook = []
    blacklist = ['10.15.187.3']
    port = 4444  # Reserve a port for your service.
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


    def customcmds(data):
        if data == "b'whosin'":
            print(addrbook)
        else:
            return False

    def newclient(conn, addr):
        data = conn.recv(1024)
        if "GET" in repr(data):
            pass
        else:
            print("From ", addr[0], ": ", repr(data))
            customcmds(repr(data))

    while True:
        conn, addr = s.accept()
        if addr[0] in blacklist:
            pass
        else:
            addrbook.append(addr[0])
            newclient(conn, addr)
    s.close()


if __name__ == "__main__":
    main()