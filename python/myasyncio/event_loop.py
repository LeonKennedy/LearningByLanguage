#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: event_loop.py
@time: 2021/4/3 9:14 上午
@desc:
"""

import asyncio
import sys
from threading import Thread


def exp1():
    loop = asyncio.new_event_loop()
    print(loop)  # <_UnixSelectorEventLoop running=False closed=False debug=False>
    asyncio.set_event_loop(loop)

    if sys.platform != "win32":
        print("platform is: ", sys.platform)
        watcher = asyncio.get_child_watcher()
        watcher.attach_loop(loop)


class LoopShoerThread(Thread):
    def run(self):
        try:
            loop = asyncio.get_event_loop() # 只可以在主进程使用。 fail throw RuntimeError
            print(loop)
        except RuntimeError:
            print("No event loop!")


def exp2():
    loop = asyncio.get_event_loop() # success
    print('e', loop)
    thread = LoopShoerThread()
    thread.start()


if __name__ == '__main__':
    exp2()
