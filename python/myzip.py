#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myzip.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 掩饰大小zip
# @Create: 2018-10-25 10:12:33
# @Last Modified: 2018-10-25 10:12:33
#

from itertools import zip_longest

a = zip(range(3), 'ABC', [5,6,7,8,9])
print(list(a))
b = zip_longest(range(3), 'ABC', [5,6,7,8,9], fillvalue = '#')
print(list(b))

