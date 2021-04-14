#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp3.py
@time: 2021/3/29 5:42 下午
@desc: Linear Blending Problem 线性混合问题
https://jckantor.github.io/ND-Pyomo-Cookbook/02.03-Linear-Blending-Problem.html
"""
import datetime

from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, maximize, Constraint, Suffix
from utils import solve

# 酒厂生产100 gallons  4% ABV(alchohol by volume) beer)
vol = 100
abv = 0.040

# 材料
material = {
    "bear A": {'abv': 0.045, 'cost': 0.32},
    "bear B": {'abv': 0.037, 'cost': 0.25},
    "water": {'abv': 0, 'cost': 0.05}
}


def beer_blend(vol, abv, data):
    C = data.keys()
    model = ConcreteModel()
    model.x = Var(C, domain=NonNegativeReals)
    model.cost = Objective(expr=sum(model.x[c] * data[c]['cost'] for c in C))
    model.vol = Constraint(expr=vol == sum(model.x[c] for c in C))
    model.abv = Constraint(expr=0 == sum(model.x[c] * (data[c]['abv'] - abv) for c in C))

    solve(model)

    print('Optimal Blend')
    for c in data.keys():
        print('  ', c, ':', model.x[c](), 'gallons')
    print()
    print('Volume = ', model.vol(), 'gallons')
    print('Cost = $', model.cost())


if __name__ == '__main__':
    beer_blend(vol, abv, material)
