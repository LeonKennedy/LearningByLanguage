#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: yieldfrom.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: yield from 的例子 
# @Create: 2018-11-04 23:16:33
# @Last Modified: 2018-11-04 23:16:33
#

def g(x):
  yield from range(x, 0, -1)
  yield from range(x)

print(list(g(5)))

def accumulate():
  total = 0
  while 1:
    nex = yield
    if nex is None:
      return total
    total += nex

def gen_totall(ds):
  while 1:
    a = yield from accumulate()
    ds.append(a) 

bb = []
acc = gen_totall(bb)
next(acc)

for i in range(1,6):
  acc.send(i)
acc.send(None)
for i in range(1,7):
  acc.send(i)
acc.send(None)
print(bb)
