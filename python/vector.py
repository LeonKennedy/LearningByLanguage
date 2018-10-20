#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: vector.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-19 17:19:30
# @Last Modified: 2018-10-19 17:19:30


from array import array
import math
class Vertor2d:

  typecode = 'd'
  def __init__(self, x,y):
    self.x = float(x)
    self.y = float(y)

  def __str__(self):
    return '(%r, %r)' % (self.x, self.y)

  def __abs__(self):
    return math.hypot(self.x,self.y)

  # bool(instance)  需要 __bool__
  def __bool__(self):
    return bool(abs(self))

  # tuple(instance) 需要实现__iter__
  def __iter__(self):
    return (i for i in (self.x, self.y))

  def __eq__(self, other):
    return tuple(self) == tuple(other)

  def __repr__(self):
    name = type(self).__name__
    return '%s(%r, %r)' % (name, *self)

  # 序列话和反序列话
  # bytes([100]) ord('d') 互相转换
  # chr   ascii(100)   ->   str('b')
  # ord   str('b')    -> ascii(100)
  def __bytes__(self):
    return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))


  @classmethod
  def formbytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    print(memv)
    return cls(*memv)


  def angle(self):
    return math.atan2(self.y, self.x)

  def __format__(self, fmt):
    if fmt.endswith('p'):
      fmt = fmt[:-1]
      coods = (abs(self), self.angle())
      outer = '<{}, {}>'
    else:
      coods = self
      outer = '({} {})'
    components = (format(c, fmt) for c in coods)
    return outer.format(*components)


if __name__ == "__main__":
  v = Vertor2d(3,4)
  print(format(v,'.5'))
  print(format(v,'.5p'))
  
