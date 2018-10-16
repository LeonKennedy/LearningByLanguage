#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myfunctools.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 主要介绍functools 的用法
# @Create: 2018-10-16 15:23:39
# @Last Modified: 2018-10-16 15:23:39


import functools, time

#wrap, reduce, partial 见其他文件

def clock(func):
  @functools.wraps(func)
  def clocked(*args, **kwargs):
    t0 = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - t0
    arg_lst = []
    if args:
      arg_lst.append(', '.join(repr(arg) for arg in args))
    if kwargs:
      pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs_items())]
      arg_lst.append(pairs)
    arg_str = ', '.join(arg_lst)
    print('[%.8fs] %s(%s) -> %r' % (elapsed, func.__name__, arg_str, result))
    return result
  return clocked

@clock
def fibonacci(n):
  return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)


# 因为lru_cache使用字典存储，所以装饰的函数，它所有参数都必须是可 hash
@functools.lru_cache()
@clock
def fibonacci2(n):
  return n if n < 2 else fibonacci2(n-2) + fibonacci2(n-1)

def lru_useage():
 
  print(fibonacci(6))
  print('same function with least recertly cache')
  print(fibonacci2(6))


# ---------------------------------------------------
import html
def htmlize(obj):
  content = html.escape(repr(obj))
  return '<pre>{}</pre>'.format(content)

if __name__ == '__main__':
  lru_useage()

