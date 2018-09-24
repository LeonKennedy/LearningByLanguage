#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: magic_method.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: __repr__ __add__ __mul__ __abs__ __bool__等魔术方法
# @Create: 2018-09-24 20:33:59
# @Last Modified: 2018-09-24 20:33:59
#

from math import hypot

class Vector:

  def __init__(self, x, y):
    self._x = x
    self._y = y

  def __repr__(self):
    return "Vector(x=%r, y=%r)" % (self._x, self._y)

  def __add__(self, other):
    x = self._x + other._x
    y = self._y + other._y
    return Vector(x,y)
  
  def __mul__(self, n):
    x = self._x * n
    y = self._y * n
    return Vector(x, y)

  def __abs__(self):
    return hypot(self._x, self._y)

  def __bool__(self):
    return bool(self._x or self._y)

if __name__ == "__main__":
  v1 = Vector(3,4)
  v2 = Vector(2,6)
  print(v1 + v2)
  print(v1 * 2)
