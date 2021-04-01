#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: experiment.py
@time: 2021/3/31 5:08 下午
@desc:
"""
import random

import numpy as np
import pandas as pd

from pyomo.environ import ConcreteModel, Set, Var, Binary, Objective, maximize, Constraint, ConstraintList, SolverFactory

teachers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lessons = [100, 101, 102, 103, 104, 105, 106]

a = np.random.randint(0, 2, size=(len(teachers), len(lessons)), dtype='uint8')
score = np.random.random((len(teachers), len(lessons))) * 5
b = pd.DataFrame(a * score, index=teachers, columns=lessons)
print(b)

room_cnt = 6
rooms = dict(zip(range(1000, 1000 + room_cnt), random.choices(lessons, k=room_cnt)))
print(rooms)

m = ConcreteModel()
m.teachers = Set(initialize=teachers)
m.lessons = Set(initialize=lessons)
m.x = Var(teachers, lessons, domain=Binary)
# m.x = Var(domain=Binary)
m.scores = Objective(expr=sum(m.x[t, l] * b.loc[t, l] for t in teachers for l in lessons), sense=maximize)

m.lb = Constraint(m.teachers, rule=lambda m, t: sum(m.x[t, l] for l in lessons) <= 1)
m.cb = Constraint(m.lessons, rule=lambda m, l: sum(m.x[t, l] for t in teachers) <= 1)

result = SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(m)
result.write()

print("score: ", m.scores())
c = []
for t in teachers:
    c.append([m.x[t, l]() for l in lessons])
d = pd.DataFrame(c, index=teachers, columns=lessons)
print(d)
