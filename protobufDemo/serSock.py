#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from socket import *

import person_pb2

pers = person_pb2.all_person()
p1 = pers.Per.add()
p1.id = 1
p1.name = 'xieyanke'
p2 = pers.Per.add()
p2.id = 2
p2.name = 'pythoner'

# 对数据进行序列化
data = pers.SerializeToString()

HOST = 'localhost'
PORT = 3333
BUFSIZ = 4096
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    tcpCliSock,addr = tcpSerSock.accept()
    # tcpCliSock.send('helloWorld'.encode())
    tcpCliSock.send(data)

    tcpCliSock.close()

tcpSerSock.close()