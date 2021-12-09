#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: server.py
@time: 2021/12/9 2:56 下午
@desc:
"""

import asyncio
import pickle


async def handle_echo(reader:asyncio.StreamReader, writer):
    data = await reader.read()
    message = pickle.loads(data)
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()


async def other_process():
    while 1:
        await asyncio.sleep(1)
        print("other process")


async def main():
    # server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    server = await asyncio.start_unix_server(handle_echo, 'unix_socket')

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    asyncio.create_task(other_process())
    async with server:
        await server.serve_forever()


asyncio.run(main())
