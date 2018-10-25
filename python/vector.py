#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: vector.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-19 17:19:30
# @Last Modified: 2018-10-19 17:19:30


from array import array
import math, pdb, functools, operator

class Vertor2d:
  
  # 转换字节序列编码
  # d 采用8字节双精度浮点
  # f 4字节单精度浮点
  typecode = 'd'
  def __init__(self, x,y):
    self._x = float(x)
    self._y = float(y)

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

  '''
  为了实现可散列 必须要实现__hash__
  必须让属性不可修改
  '''

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y


import reprlib, numbers


class Vector:
  typecode = 'd'
  def __init__(self, component):
    self._component = array(self.typecode, component)

  def __iter__(self):
    return iter(self._component)

  def __repr__(self):
    components = reprlib.repr(self._component)
    components = components[components.find('['):-1]
    return 'Vector({})'.format(str(components))

  def __str__(self):
    return str(tuple(self))

  def __eq__(self, other):
    if len(self) != len(other):
      return False
    return all(a == b for a, b in zip(self,other))

  def __hash__(self):
    hashes = (hash(x) for x in self._component)
    return functools.reduce(operator.xor, hashes, 0)

  def __bytes__(self):
    return (bytes([ord(self.typecode)]) + bytes(self._component))

  def __bool__(self):
    return bool(abs(self))

  def __abs__(self):
    return math.sqrt(sum(x * x for x in self))

  @classmethod
  def formbytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(memv)

  def __len__(self):
    return len(self._component)

  def __getitem__(self, index):
    cls = type(self)
    if isinstance(index, slice):
      return cls(self._component[index])
    elif isinstance(index, numbers.Integral):
      return self._component[index]
    else:
      msg = '{cls.__name__} indices must be integral'
      raise TypeError(msg.format(cls= cls))

if __name__ == "__main__":
  v = Vertor2d(3,4)
  print(format(v,'.5'))
  print(format(v,'.5p'))
  
