#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myzip.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 掩饰大小zip
# @Create: 2018-10-25 10:12:33
# @Last Modified: 2018-10-25 10:12:33
#

from itertools import zip_longest, takewhile, count, dropwhile, islice

#a = zip(range(3), 'ABC', [5,6,7,8,9])
b = zip_longest(range(3), 'ABC', [5,6,7,8,9], fillvalue = '#')
print(list(b))

#-----------
#----- count  是无限生成器
gen = takewhile(lambda x: x < 4, count(1, .5))
print(list(gen))

# ---------
def vowel(c):
  return c.lower() in 'aeiou'

c = filter(vowel, 'Aardvark')
print(list(c))  #['A', 'a', 'a']
c = dropwhile(vowel, 'Aardvark')
print(list(c)) # ['r', 'd', 'v', 'a', 'r', 'k']
c = takewhile(vowel, 'Aardvark')
print(list(c))  # ['A', 'a']
# 切片所有对象
c = islice('Aardvark', 4)
print(list(c))  # ['A', 'a', 'r', 'd']
c = islice('Aardvark', 4, 7)
print(list(c)) # ['v', 'a', 'r']
c = islice('Aardvark', 1, 7, 2)
print(list(c)) # ['a', 'd', 'a']

# --------
from itertools import accumulate
sample = [5,2,3,6,8,1,4,9, 7]
d = accumulate(sample)
print(list(d))  # [5, 7, 10, 16, 24, 25, 29, 38, 45]
d = accumulate(sample, min)
print(list(d))  # [5, 2, 2, 2, 2, 1, 1, 1, 1]
d = accumulate(sample, max)
print(list(d))  # [5, 5, 5, 6, 8, 8, 8, 9, 9]
import operator
d = accumulate(sample, operator.mul)
print(list(d))  # [5, 10, 30, 180, 1440, 1440, 5760, 51840, 362880]

# ----- 
from itertools import starmap
e = starmap(operator.mul, enumerate('awBnde', 1))
print(list(e)) # ['a', 'ww', 'BBB', 'nnnn', 'ddddd', 'eeeeee']
e = starmap(lambda a,b : b / a, enumerate(accumulate(sample), 1))
print(list(e))  # 平均数  [200~[5.0, 3.5, 3.3333333333333335, 4.0, 4.8, 4.166666666666667, 4.142857142857143, 4.75, 5.0]

