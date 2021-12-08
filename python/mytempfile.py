#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: mytempfile.py
@time: 2021/10/4 6:55 下午
@desc:
"""
import tempfile


f = tempfile.TemporaryFile()

f.write(b'12345')
print(f.tell())
f.write(b'67')
print(f.tell())
f.seek(-3, 1)
a = f.read(2)
print(a)