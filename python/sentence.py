#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: sentence.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-29 18:25:36
# @Last Modified: 2018-10-29 18:25:36
#

import re, reprlib, abc, pdb
from collections import Iterator

RE_WORD = re.compile('\w+')

class Sentence:
  def __init__(self, text):
    self.text = text
    #self._words = text.split(' ')
    self._words = RE_WORD.findall(self.text)

  def __getitem__(self, index):
    return self._words[index]

  def __len__(self):
    return len(self._words)

  def __repr__(self):
    return 'Sentence(%s)' % reprlib.repr(self.text)  # 大型字符串 缩略

  def __iter__(self):
    return SentenceIterator(self._words)

class SentenceIterator:
  
  index  = 0
  def __init__(self, words):
    self.words = words

  def __next__(self):
    try:
      word = self.words[self.index]
    except IndexError:
      raise StopIteration()
    self.index += 1
    return word

  def __iter__(self):
    return self


#1. 带yield都是生成器函数，返回生成器，可迭代
#2. 读取文件也可以用惰性
class Sentence2:

  def __init__(self, text):
    self._text = text

  def __repr__(self):
    return 'Sentence(%s)' % reprlib.repr(self.text)  # 大型字符串 缩略

  def __iter__(self):
    for match in RE_WORD.finditer(self._text):
      yield match.group()

if __name__ == "__main__":
  text ='sdfjie "ni hao a wo shi ni baba" , jeidj'
  s = Sentence2(text)
  for i in s:
    print(i)


