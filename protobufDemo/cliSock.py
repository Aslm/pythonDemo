from socket import *

import person_pb2

receive_pro_buf = person_pb2.all_person()

HOST = 'localhost'
PORT = 3333
BUFSIZ = 4096
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)


while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    receive_pro_buf.ParseFromString(data)
    print(receive_pro_buf)

print
'Done!'
tcpCliSock.close()