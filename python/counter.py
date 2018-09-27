#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: counter.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-09-27 16:33:03
# @Last Modified: 2018-09-27 16:33:03
#


import collections

ct = collections.Counter('ctvygbuhnafdvubiawf')
print(ct)
ct['v'] += 1
ct.update('cytvbu')
print(ct)
print(ct.most_common(3))
print(dir(ct))


ct2 = collections.Counter('my name is coffee')
print(ct2)
