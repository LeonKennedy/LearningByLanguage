#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: myactor.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-09-20 17:27
# @Last Modified: 2019-09-20 17:27


import pykka


class Calculator(pykka.ThreadingActor):
    def __init__(self):
        super().__init__()
        self.last_result = None

    def add(self, a, b=None):
        if b is not None:
            self.last_result = a + b
        else:
            self.last_result += a
        return self.last_result

    def sub(self, a, b=None):
        if b is not None:
            self.last_result = a - b
        else:
            self.last_result -= a
        return self.last_result

    def on_receive(self, message):
        return 'Hi there!'

if __name__ == '__main__':
    actor_ref = Calculator.start()
