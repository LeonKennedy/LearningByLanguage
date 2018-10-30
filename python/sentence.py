#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: sentence.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-10-29 18:25:36
# @Last Modified: 2018-10-29 18:25:36
#

import re, reprlib

RE_WORD = re.compile('\w+')

class Sentence:
  def __init__(self, text):
    self.text = text
    self._words = text.split(' ')

  def __getitem__(self, index):
    return self._words[index]

  def __len__(self):
    return len(self._words)

  def __repr__(self):
    return 'Sentence(%s)' % reprlib.repr(self.text)  # 大型字符串 缩略

if __name__ == "__main__":
  text = "ni hao a wo shi ni baba"
  s = Sentence(text)
  print(s[2])
  print(s)


