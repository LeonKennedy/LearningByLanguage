#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: spinner_thread.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 多线程和异步的对比
# @Create: 2018-12-10 10:29:31
# @Last Modified: 2018-12-10 10:29:31


import threading, asyncio
import itertools, time, sys, pdb

#  --------------  threading --------------
class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break

    write(' ' * len(status) + '\x08' * len(status))

def slow_function():
    time.sleep(3)
    return 32

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin,
                                args=('thinking!olenji', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result

def main():
    result = supervisor()
    print('Answer:', result)

# ------------- asyncio --------------
@asyncio.coroutine
def spin_async(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    write(' ' * len(status) + '\x08' * len(status))

@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)  # sleep without blocking
    return 42

@asyncio.coroutine
def supervisor_async():
    spinner = asyncio.async(spin_async('thinking!'))
    print('spinner object:', spinner)
    result = yield from slow_function()
    spinner.cancel()  # Task对象课可以取消
    return result

def main_async():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor_async())
    loop.close()
    print('Answer:', result)




if __name__ == '__main__':
    main_async()
