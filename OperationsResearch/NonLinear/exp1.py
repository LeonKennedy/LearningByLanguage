#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp1.py
@time: 2021/7/7 10:36 上午
@desc:
"""
from pyomo.environ import *

model = ConcreteModel()
model.x = Var(initialize=1.5)
model.y = Var(initialize=1.5)


def rosenbrock(m):
    return (1.0 - m.x) ** 2 + 100.0 * (m.y - m.x ** 2) ** 2


model.obj = Objective(rule=rosenbrock, sense=minimize)
SolverFactory('ipopt', excutable="/usr/local/bin/ipopt").solve(model, tee=True)
model.pprint()
print("x:", model.x(), "y:", model.y())
print("object:", model.obj())
