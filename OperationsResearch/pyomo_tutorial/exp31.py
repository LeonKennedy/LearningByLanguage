#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp31.py
@time: 2021/3/31 11:36 上午
@desc:
"""

from pyomo.environ import ConcreteModel, Set, Var, NonNegativeReals, Objective, minimize, Constraint, ConstraintList, TransformationFactory
from utils import solve
Demand = {
    'Lon': 125,  # London
    'Ber': 175,  # Berlin
    'Maa': 225,  # Maastricht
    'Ams': 250,  # Amsterdam
    'Utr': 225,  # Utrecht
    'Hag': 200  # The Hague
}

Supply = {
    'Arn': 600,  # Arnhem
    'Gou': 650  # Gouda
}

T = {
    ('Lon', 'Arn'): 1000,
    ('Lon', 'Gou'): 2.5,
    ('Ber', 'Arn'): 2.5,
    ('Ber', 'Gou'): 1000,
    ('Maa', 'Arn'): 1.6,
    ('Maa', 'Gou'): 2.0,
    ('Ams', 'Arn'): 1.4,
    ('Ams', 'Gou'): 1.0,
    ('Utr', 'Arn'): 0.8,
    ('Utr', 'Gou'): 1.0,
    ('Hag', 'Arn'): 1.4,
    ('Hag', 'Gou'): 0.8
}

m = ConcreteModel()
de_k = Demand.keys()
su_k = Supply.keys()

m.x = Var(de_k, su_k, domain=NonNegativeReals)
m.dis = Objective(expr=sum(m.x[i] * v for i, v in T.items()), sense=minimize)

m.cons = ConstraintList()
for i in de_k:
    m.cons.add(expr=sum( m.x[i,j] for j in su_k) == Demand[i])

for j in su_k:
    m.cons.add(expr=sum( m.x[i,j] for i in de_k) <= Supply[j])

result = solve(m)
print(f"distance: {m.dis()}")


for i in T:
    print(i, m.x[i]())