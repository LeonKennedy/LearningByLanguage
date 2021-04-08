#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp2.py
@time: 2021/3/29 4:58 下午
@desc: sensitivity analysis 灵敏度分析
"""
from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, maximize, Constraint, Suffix
from utils import solve


def exp1():
    model = ConcreteModel()

    # for access to dual solution for constraints
    model.dual = Suffix(direction=Suffix.IMPORT)

    # declare decision variables
    model.x = Var(domain=NonNegativeReals)
    model.y = Var(domain=NonNegativeReals)

    # declare objective
    model.profit = Objective(
        expr=40 * model.x + 30 * model.y,
        sense=maximize)

    # declare constraints
    model.demand = Constraint(expr=model.x <= 40)
    model.laborA = Constraint(expr=model.x + model.y <= 80)
    model.laborB = Constraint(expr=2 * model.x + model.y <= 100)

    # solve
    solve(model)

    print("\nSolution")
    print(f"profit = {model.profit()}")
    print(f"x = {model.x()}")
    print(f"y = {model.y()}")

    print("\nSensitivity Analysis")
    print(f"y_demand = {-model.dual[model.demand]}")
    print(f"y_laborA = {-model.dual[model.laborA]}")
    print(f"y_laborB = {-model.dual[model.laborB]}")

    str = "   {0:7.2f} {1:7.2f} {2:7.2f} {3:7.2f}"

    print("Constraint  value  lslack  uslack    dual")
    for c in [model.demand, model.laborA, model.laborB]:
        print(c, str.format(c(), c.lslack(), c.uslack(), model.dual[c]))


def exp2():
    model = ConcreteModel()


if __name__ == '__main__':
    exp1()
