#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: mysocket.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2017-06-07 08:56:45
# @Last Modified: 2017-06-07 08:56:45
#

import socket, sys, time,pdb


def socket_server():
    sk = socket.socket()
    sk.bind(("127.0.0.1",8030))
    sk.listen(5)

    conn,address = sk.accept()
    print(address)
    cont = 'Hello world'
    conn.send(bytes(cont))

def socket_client():
    obj = socket.socket()
    obj.connect(("127.0.0.1",8030))

    ret = obj.recv(1024).decode("utf-8")
    print(ret)


if __name__ == "__main__":
    if len(sys.argv) ==  2 and sys.argv[1]== 'server':
        print("sever...")
        socket_server()
    else:
        print("client...")
        socket_client()
