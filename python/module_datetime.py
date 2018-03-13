#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: module_datetime.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: datetime 的使用
# @Create: 2018-03-13 15:48:35
# @Last Modified: 2018-03-13 15:48:35
#

import datetime, calendar

today = datetime.date.today()
# 2018-03-13
weekday = today.weekday()
# 1
sunday = today - datetime.timedelta(days=weekday+1)
# 2018-03-11    -> weekday  6

#(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
if weekday == calendar.TUESDAY:
  print('Today is Tuesday')
else:
  print('weekday() is %d' %today.weekday())
  print('calendar.MONDAY is %d' % calendar.MONDAY)
  print('calendar.TUESDAY is %d' % calendar.TUESDAY)
  print('calendar.FRIDAY is %d' % calendar.FRIDAY)
  print('calendar.SATURDAY is %d' % calendar.SATURDAY)
  print('calendar.SUNDAY is %d' % calendar.SUNDAY)


'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

def get_weekdays(year, week):
  week_name = '%d-%d' % (year, week)
  move_day = datetime.date(year, 1,1)
  oneday = datetime.timedelta(days = 1)
  while move_day.strftime('%Y-%W') != week_name:
    move_day += oneday
  return [ move_day + datetime.timedelta(days = i) for i in range(7)]



#返回指定年的某月
def get_month(year, month):
  return calendar.month(year, month)

#返回指定年的日历
def get_calendar(year):
  return calendar.calendar(year)

#判断某一年是否为闰年，如果是，返回True，如果不是，则返回False
def is_leap(year):
  return calendar.isleap(year)

#返回某个月的weekday的第一天和这个月的所有天数
def get_month_range(year, month):
  return calendar.monthrange(year, month)

#返回某个月以每一周为元素的序列
def get_month_calendar(year, month):
  return calendar.monthcalendar(year, month)

def calendar_main():
  year = 2018
  month = 8
  test_month = get_month(year, month)
  print(test_month)
  print('#' * 50)
  #print(get_calendar(year))
  print('{0}这一年是否为闰年？：{1}'.format(year, is_leap(year)))
  print(get_month_range(year, month))
  print(get_month_calendar(year, month))
                                     
if __name__ == '__main__':
  pass

