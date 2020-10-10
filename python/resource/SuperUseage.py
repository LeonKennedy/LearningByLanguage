#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: SuperUseage.py
@time: 2020/6/12 10:41 上午
@desc:
"""

import collections

class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Cant delete attribute")


class SubPerson(Person):

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to ', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


class ErrorPerson(Person):
    # ERROR
    # @property
    # def name(self):
    #     print('Getting name')
    #     return super().name

    # 可以改写成这样
    @Person.name.getter
    def name(self):
        print('Getting name')
        return Super().name


if __name__ == "__main__":
    s = ErrorPerson('Coffee')
    s.name
