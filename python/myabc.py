#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: myabc.py
@time: 2021/12/8 5:50 下午
@desc:
"""
from abc import abstractmethod, ABC


class A(ABC):
    def hello(self):
        print("hello")

    @abstractmethod
    def speak(self):
        print("speak")


class B(A):

    def speak(self):
        print("speak")


if __name__ == '__main__':
    b= B()
    b.speak()
    # a = A() # error
