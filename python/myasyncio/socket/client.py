#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: client.py
@time: 2021/12/9 3:03 下午
@desc:
"""
import asyncio
import time
import pickle
import socket


# async def tcp_echo_client(data):
#     # reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
#     reader, writer = await asyncio.open_unix_connection("unix_socket")
#
#     writer.write(pickle.dumps(data))
#     writer.write_eof()
#
#     data = await reader.read()
#     print(f'Received: {data.decode()!r}')
#
#     print('Close the connection')
#     writer.close()
#
#
# asyncio.run(tcp_echo_client({"slot": "dsfjie", "Business": 7}))


def unix_client(data):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect("unix_socket")
        s.sendall(pickle.dumps(data))
        s.shutdown(socket.SHUT_WR)
        received = bytes()
        while 1:
            block = s.recv(100)
            if block == b'':
                break
            received += block
        msg = pickle.loads(received)
    print('Received', msg)


unix_client({"slot": "dsfjie", "Business": 7})
