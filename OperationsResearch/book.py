#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: book.py
@time: 2021/3/29 5:10 下午
@desc:
"""
from pyomo.environ import SolverFactory, ConcreteModel, Var, NonNegativeReals, Objective, maximize, Constraint, \
    SolverFactory, minimize


def solve(model):
    return SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model)


def exp1():
    """
    Page 15
    :return:
    """
    model = ConcreteModel()
    model.x1 = Var(domain=NonNegativeReals)
    model.x2 = Var(domain=NonNegativeReals)

    model.profit = Objective(expr=model.x1 * 2 + model.x2 * 3, sense=maximize)

    model.eq = Constraint(expr=model.x1 + model.x2 * 2 <= 8)
    model.origin_A = Constraint(expr=model.x1 * 4 <= 16)
    model.origin_B = Constraint(expr=model.x2 * 4 <= 12)

    result = SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model)

    print("\nSolution")
    print(f"profit = {model.profit()}")
    print(f"x1 = {model.x1()}")
    print(f"x2 = {model.x2()}")


def exp2():
    "page 42  例8"
    model = ConcreteModel()
    model.x = Var(domain=NonNegativeReals)
    model.y = Var(domain=NonNegativeReals)
    model.z = Var(domain=NonNegativeReals)

    model.profit = Objective(expr=model.x * -3 + model.y + model.z, sense=minimize)

    model.eq = Constraint(expr=model.x - 2 * model.y + model.z <= 11)
    model.origin_A = Constraint(expr=-4 * model.x + model.y + 2 * model.z >= 3)
    model.origin_B = Constraint(expr=-2 * model.x + model.z == 1)

    result = SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model)

    print("\n==Solution==")
    print(f"profit = {model.profit()}")
    print(f"x = {model.x()}, y = {model.y()}, z = {model.z()} ")


if __name__ == '__main__':
    exp2()
