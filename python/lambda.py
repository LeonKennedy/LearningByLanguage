#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: lambda.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2017-04-20 17:35:45
# @Last Modified: 2017-04-20 17:35:45
#

import re
a = "//s.taobao.com/list?spm=a21bo.7723600.26093.73.yOEzqZ&q=%E6%B0%9F%E8%8B%AF%E5%B0%BC%E8%80%83&mid=5868&cat=56170009%2C56136008%2C56162003" 
aa = "//list.taobao.com/itemlist/acg.htm?cat=54332006%2C54428001%2C54538002%2C54450006%2C54514006%2C54434003%2C54442005%2C54436003&isprepay=1&user_type=0&sd=1&viewIndex=1&as=0&spm=a21bi.1289946.1998155313.29.Qr4QcK&hd=1&atype=b&style=grid&q=%E6%B5%B7%E8%B4%BC%E7%8E%8B&same_info=1&isnew=2&filter=reserve_price[30%2C100000000]&tid=0&_input_charset=utf-8"

c = [ b for b in aa.replace('?','&').split('&') if b[0:4] == "cat="][0]


print c
