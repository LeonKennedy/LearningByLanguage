#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: format.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-20 16:11:06
# @Last Modified: 2018-10-20 16:11:06
#

from vector import Vertor2d

'''
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.
'''
b = "first {0} second {1} third {0} with {{aa}}".format(1,2)
print(b)
cc = [4,5,6]
c = "first {ma[0]} second {ma[1]} ".format(ma=cc)
print(c)
c1 = "first {0[1]} second {0[2]} with no key".format(cc)
print(c1)

'''
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first
'''

v = Vertor2d(3,4)
d = "Harold's a clever {0!s}".format(v)
e = "Bring out the holy {0!r}".format(v)
print(d)
print(e)

print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered')) 

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

print('Correct answers: {:.2%}'.format(38/65))
print('Correct answers: {:.2}'.format(38/65))


d = dict(who='tim', what='swim')
print('{who} like {what}'.format(d))

import datetime
d = datetime.datetime(2018, 10, 20, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))


from string import Template
s = Template('$who likes $what')
q = s.substitute(who='tim', what='kung pao')
print(q)
d = dict(who='tim')
# e = Template('$who likes $what').substitute(d) 
# KeyError: 'what'
r = Template('$who likes $what').safe_substitute(d)
print(r)
