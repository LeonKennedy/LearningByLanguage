#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: mydatetime.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: datetime 小例子
# @Create: 2018-06-09 21:57:15
# @Last Modified: 2018-06-09 21:57:15
#

import datetime
now = datetime.datetime.now()
print(now)
print(now.isoformat())
str_now = now.strftime('%Y-%m-%d %H:%M:%S')
print(str_now)

print('换成第一天')
now.replace(day=1)
print(now.replace(day=1))

print('换成5月')
print(now.replace(month=5))
#print(now.replace(year=1))

print('减一天')
lastday = now - datetime.timedelta(days=1)
print(lastday)
