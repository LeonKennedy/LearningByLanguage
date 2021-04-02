#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp1.py
@time: 2021/3/29 4:31 下午
@desc:
"""

from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, maximize, Constraint, SolverFactory
from .utils import solve


def exp1():
    """
     Production Models with Linear Constraints (https://jckantor.github.io/ND-Pyomo-Cookbook/02.01-Production-Models-with-Linear-Constraints.html)
    生产产品x 单价270, 市场容量 40，
    x的成本 100原材料成本 1小时人工A  2小时人工B
    人工A  每周80小时上限  cost 50/hour
    人工B  每周100小时上限  cost 40/hour
    问每周最大利益？

    profie  = 270 * x - (100 + 50 + 40*2) * x
            = 40x
    """
    model = ConcreteModel()
    model.x = Var(domain=NonNegativeReals)

    model.profit = Objective(expr=40 * model.x, sense=maximize)

    model.demand = Constraint(expr=model.x <= 40)
    model.laborA = Constraint(expr=model.x <= 80)
    model.laborB = Constraint(expr=model.x <= 100)

    SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model).write()

    print("Profit = ", model.profit(), " per week")
    print("X = ", model.x(), " units per week")


def exp2():
    """
    生产产品x 单价210
    x的成本 90原材料成本 1小时人工A  1小时人工B
    人工A  每周80小时上限  cost 50/hour
    人工B  每周100小时上限  cost 40/hour
    问每周最大利益？

    profie  = 210 * x - (90 + 50 + 40) * x
            = 30x
    :return:
    """
    model = ConcreteModel()
    model.y = Var(domain=NonNegativeReals)
    model.profit = Objective(expr=30 * model.y, sense=maximize)
    model.laborA = Constraint(expr=model.y <= 80)
    model.laborB = Constraint(expr=model.y <= 100)

    solve(model)

    print("Profit = ", model.profit(), " per week")
    print("Y = ", model.y(), " units per week")


def exp3():
    """
    生产两种产品x, y 最大利益
    :return:
    """
    model = ConcreteModel()
    model.x = Var(domain=NonNegativeReals)
    model.y = Var(domain=NonNegativeReals)
    model.profit = Objective(expr=30 * model.y + 40 * model.x, sense=maximize)
    model.demand = Constraint(expr=model.x <= 40)
    model.laborA = Constraint(expr=model.x + model.y <= 80)
    model.laborB = Constraint(expr=2 * model.x + model.y <= 100)

    solve(model)

    print("Profit = ", model.profit(), " per week")
    print("X = ", model.x(), " units per week")
    print("Y = ", model.y(), " units per week")



if __name__ == '__main__':
    exp3()
