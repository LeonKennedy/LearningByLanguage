#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: lambda.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 闭包
# @Create: 2017-04-20 17:35:45
# @Last Modified: 2017-04-20 17:35:45
#

def outer(a):
    def inner(b):
        return max(a) * b

    return inner


bf = outer([1, 2, 3])
x = bf(2)
print(x)

c = [1, 2, 3, 4]


def single(a):
    return a


cf = lambda: single(4)
x = cf()
print(x)
