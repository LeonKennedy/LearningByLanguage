#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: Tombola.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 抽象类的使用例子（不建议继承抽象类， 实现协议即可)
# @Create: 2018-10-26 21:43:56
# @Last Modified: 2018-10-26 21:43:56

import abc
import pdb
import random


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        '''把元素放入容器'''

    @abc.abstractmethod
    def pick(self):
        '''随机取出一个元素'''

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


# subclass 1
class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick form empty BingeCage')

    def __call__(self):
        return self.pick()


# virtual class

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


# ==============  test ================
import doctest

TEST_FILE = 'tombola_test.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):
    verbose = '-v' in argv
    real_subclass = Tombola.__subclasses__()
    virtual_subclasses = list(Tombola._abc_registry)

    for cls in real_subclass + virtual_subclasses:
        pdb.set_trace()
        test(cls, verbose)


def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == "__main__":
    import sys

    main(sys.argv)
