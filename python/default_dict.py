#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: default_dict.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-09-27 15:51:33
# @Last Modified: 2018-09-27 15:51:33
#

a = dict([('a',[1,2]), ('b', [3,4])])
a.setdefault('c', []).append(5)
print(a)


import collections
d = collections.defaultdict(list)
d['c'].append(5)
print(d)

