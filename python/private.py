#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: private.py
@time: 2020/10/6 1:53 上午
@desc:
"""


class A:
    def __init__(self):
        self.__age = 18


if __name__ == '__main__':
    a = A()
    # print(a.__age) # can't use
    print(a._A__age)
