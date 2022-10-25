#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: sample.py
@time: 2021/4/15 4:11 下午
@desc:
"""

import numpy as np
import geatpy as ea


class AssignProblem(ea.Problem):
    def __init__(self):
        name = "assign"
        maxormins = [1]
        Dim = 16
        varTypes = [1] * Dim
        lb = [0] * Dim
        ub = [1] * Dim
        lbin = [1] * Dim
        ubin = [1] * Dim
        ea.Problem.__init__(self, name, 1, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):
        Vars = pop.Phen

