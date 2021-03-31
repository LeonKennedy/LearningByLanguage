#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: utils.py
@time: 2021/3/29 5:03 下午
@desc:
"""

from pyomo.environ import SolverFactory
from pyomo.opt import SolverResults


def solve(model) -> SolverResults:
    return SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model)
