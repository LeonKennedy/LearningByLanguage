#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: coroutine_gevent.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-09-10 15:54:42
# @Last Modified: 2018-09-10 15:54:42
#

import gevent

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()