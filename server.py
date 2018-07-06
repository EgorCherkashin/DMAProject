import socket


def main():
    addrbook = []
    blacklist = ['']
    port = 9999 # Reserve a port for your service.
    s = socket.socket()# Create a socket object
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


    def sentserver(ip, mes, addrbook):
        port2 = 3333 # Reserve a port for your service.
        s2 = socket.socket()# Create a socket object
        s2.bind(('', port2))  # Bind to the port
        s2.listen(5)
        sock = socket.socket()
        sock.connect((ip, port2))
        mes_enc = mes.encode()
        sock.send(mes_enc)
        print("sent to ", ip)
        sock.close()
        # myip = ['127.0.0.1', '192.168.1.106']
        # if len(addrbook) == 1:
        #     pass
        # else:
        #     if ip in myip:
        #         print(addrbook)
        #         for i in addrbook:
        #             if i != myip[0] and i != myip[1]:
        #                 print(i)
        #                 port = 3333
        #                 sock = socket.socket()
        #                 sock.connect((ip, port))
        #                 mes_enc = mes.encode()
        #                 sock.send(mes_enc)
        #                 print("sent to ", ip)
        #                 sock.close()

#---------------------------------------------------                        
            # elif ip == '10.15.187.253':
            #     print(addrbook)
            #     for i in addrbook:
            #         if i != ip:
            #             print(i)
            #             port = 3333
            #             sock = socket.socket()
            #             sock.connect((ip, port))
            #             mes_enc = mes.encode()
            #             sock.send(mes_enc)
            #             sock.close()
            # else:
            #     print("Else", addrbook)
            #     print('IP:', ip)
            #     port = 3333
            #     sock = socket.socket()
            #     sock.connect((ip, port))
            #     mes_enc = mes.encode()
            #     sock.send(mes_enc)
            #     sock.close()

    def checkinaddr(data, addrbook):
        if data in addrbook:
            return False
        else:
            return True

    def customcmds(data):
        if data == "b'whosin'":
            print(addrbook)
        else:
            return False

    def newclient(conn, addr, addrbook):
        data = conn.recv(1024)
        if "GET" in repr(data):
            pass
        elif repr(data)[0] == '~':
            pass
        else:
            printingthis = repr(data)[1:]
            print(printingthis, "--->", printingthis)
            print("From ", addr[0], ": ", repr(data))
            for i in range(len(addrbook)):
                sentserver(addrbook[i], '~'+repr(data), addrbook)
                customcmds(repr(data))

    while True:
        conn, addr = s.accept()
        if addr[0] in blacklist:
            pass
        else:
            if checkinaddr(addr[0], addrbook) == True:
                addrbook.append(addr[0])
            else:
                pass
            newclient(conn, addr, addrbook)
    s.close()


if __name__ == "__main__":
    main()