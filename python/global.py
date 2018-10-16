#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: global.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-16 08:33:20
# @Last Modified: 2018-10-16 08:33:20
#

from dis import dis
def f1():
  a = 3
  print(a)
  print(b)

def f2():
  a = 3
  print(a)
  print(b)
  b = 4


print(' ----- function 1 ------- ')
dis(f1)
print(' ----- function 2 ------- ')
dis(f2)
