#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myarray.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-09-25 16:58:09
# @Last Modified: 2018-09-25 16:58:09
#

from array import array
from random import random

floats = array('d', (random() for i in (range(10**4))))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**4)
fp.close()
print(floats2[-1])

assert floats2 == floats
