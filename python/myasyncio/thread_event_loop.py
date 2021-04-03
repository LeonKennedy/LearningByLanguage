#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: thread_event_loop.py
@time: 2021/4/3 10:01 上午
@desc: 为每一个线程创建一个绑定到线程的循环并可以等待其完成
"""

import asyncio
import threading


def create_event_loop(worker, *args, **kwargs):
    def _worker(*args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(worker(*args, **kwargs))
        finally:
            loop.close()

    return threading.Thread(target=_worker, args=args, kwargs=kwargs)


async def print_coro(*args, **kwargs):
    print(f"Inside the print coro on {threading.get_ident()}", (args, kwargs))


def start_threads(*threads):
    [t.start() for t in threads if isinstance(t, threading.Thread)]


def join_threads(*threads):
    [t.join() for t in threads if isinstance(t, threading.Thread)]


def main():
    workers = [create_event_loop(print_coro) for i in range(10)]
    start_threads(*workers)
    join_threads(*workers)


if __name__ == '__main__':
    main()
