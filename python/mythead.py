#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: mythead.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2017-03-16 11:56:59
# @Last Modified: 2017-03-16 11:56:59
#

import threading, time


class Flag:
    alive = True


def func(flag):
    count = 0
    while(flag.alive):
        print(count)
        count += 1
        time.sleep(1)

f = Flag()
t = threading.Thread(target=func, args = (f,), name = 1)
t.start()
print(dir(t))
print(t)
time.sleep(3)
f.alive = False

