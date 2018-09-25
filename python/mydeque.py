#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: mydeque.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-09-25 18:43:21
# @Last Modified: 2018-09-25 18:43:21
#

from collections import deque

dp = deque(range(10), maxlen=10)
print(dp)
dp.rotate(3)
print(dp)
dp.rotate(-4)
print(dp)

print('appendleft(-1)')
dp.appendleft(-1)
print(dp)

print('extend(11,22,33])')
dp.extend([11,22,33])
print(dp)

print('extendleft([10,20,30,40])')
dp.extendleft([10,20,30,40])
print(dp)


