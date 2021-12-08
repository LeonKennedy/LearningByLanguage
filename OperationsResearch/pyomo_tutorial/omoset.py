#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: omoset.py
@time: 2021/4/2 9:10 上午
@desc:
"""

from pyomo.environ import ConcreteModel, Set, Var, NonNegativeReals, Objective, minimize, Constraint, Boolean, \
    ConstraintList, TransformationFactory

model = ConcreteModel()
model.IDX = Set(initialize=[1, 2, 4])
model.IDX2 = model.IDX * model.IDX
print("IDX2")
for i in model.IDX2:
    print(i)

H_init = {}
H_init[2] = [1, 3, 5]
H_init[3] = [2, 4, 6]
H_init[4] = [3, 5, 7]
model.H = Set([2, 3, 4], initialize=H_init)
print('omo set')
for i in model.H:
    print(i, [j for j in model.H[i]])
