#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: doctest.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 使用doctest
# @Create: 2018-09-24 15:05:47
# @Last Modified: 2018-09-24 15:05:47
#

def plus(v1, v2):
  """
  >>> plus(3,4)
  6
  """
  return v1 + v2

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)

