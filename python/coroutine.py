#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: corout.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2018-09-10 15:17:39
# @Last Modified: 2018-09-10 15:17:39
#

import time


def A():
    while True:
        print("----A---")
        yield
        time.sleep(1)


def B(c):
    while True:
        print("----B---")
        c.__next__()
        time.sleep(1)


if __name__ == '__main__':
    a = A()
    B(a)
