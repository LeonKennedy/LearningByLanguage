#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myweakref.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 弱引用
# @Create: 2018-10-17 15:38:48
# @Last Modified: 2018-10-17 15:38:48

class Cheese:
  def __init__(self, kind):
    self.kind = kind

  def __repr__(self):
    return 'Cheese(%r)' % self.kind

import weakref

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Lercier'), Cheese('Tielet'), Cheese('Brei'), Cheese('Pramene')]
for cheese in catalog:
  stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
print('delete ref cheese:(%r)' % cheese)
del cheese
print(sorted(stock.keys()))
