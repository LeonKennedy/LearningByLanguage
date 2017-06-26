#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: bloomfilter.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:  布隆过滤器的小例子
# @Create: 2017-05-19 16:39:29
# @Last Modified: 2017-05-19 16:39:29
#

from pybloomfilter import BloomFilter
import pdb

bf = BloomFilter(10000, 0.01, 'filter.bloom')
bf.add('apple')
bf.add('pineapple')
bf.add(('watermelon','grapes'))

print('pear' in bf)   # False
print('grapes' in bf)   # False
bf.update(('watermelon','grapes'))
print('grapes' in bf)   # True

