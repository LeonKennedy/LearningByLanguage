#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myfunctools.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-04 22:12:53
# @Last Modified: 2018-10-04 22:12:53
#

from functools import reduce
from operator import add,mul

assert reduce(add, range(10))  == 45
assert reduce(mul, range(1,4)) == 6

data = [
  ('China', 1, 'aaaa'),
  ('Tokyo', 2, 'cccc'),
  ('USA', 3, 'bbbb')
]

from operator import itemgetter
for i in sorted(data, key=itemgetter(2)):
  print(i)

print('=' * 10)
mash = itemgetter(0,2)
for i in data:
  print(mash(i))

from collections import namedtuple
print('=' * 10)
LatLong = namedtuple('LatLong', 'Lat Long')
Metropolis = namedtuple('Metropolis', 'name, cc, coor')

m = Metropolis(name = 'China', cc='CN', coor=LatLong(Lat=12, Long=34))
from operator import attrgetter
mash = attrgetter('name', 'coor.Long')
print(mash(m))


print('=' * 10)
a = 'this is a apple'
from operator import methodcaller
upcase = methodcaller('upper')
print(upcase(a))
recase = methodcaller('replace',' ','-')
print(recase(a))


from functools import partial
partmul = partial(mul, 3)
print(partmul(4))
print([ partmul(i) for i in range(7)])
#parialmethod
