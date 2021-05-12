#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: property_cache.py
@time: 2021/5/12 10:32 上午
@desc:
"""
import functools

class Data:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @functools.cached_property
    def sum_out(self):
        print("sum running once")
        return self.x + self.y


if __name__ == '__main__':
    d = Data(1, 2)
    print(d.sum_out)
    print(d.sum_out)
