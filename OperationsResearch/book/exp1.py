#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp1.py
@time: 2021/3/29 5:10 下午
@desc:
"""
from pyomo.core import Suffix
from pyomo.environ import SolverFactory, ConstraintList, ConcreteModel, Var, NonNegativeIntegers, NonNegativeReals, \
    Objective, maximize, \
    Constraint, \
    SolverFactory, minimize
import pandas as pd


def solve(model):
    return SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model)


def exp1():
    """
    Page 15
    :return:
    """
    model = ConcreteModel()
    model.dual = Suffix(direction=Suffix.IMPORT)

    model.x1 = Var(domain=NonNegativeReals)
    model.x2 = Var(domain=NonNegativeReals)

    model.profit = Objective(expr=model.x1 * 2 + model.x2 * 3, sense=maximize)

    model.equipment = Constraint(expr=model.x1 + model.x2 * 2 <= 10)
    model.origin_A = Constraint(expr=model.x1 * 4 <= 16)
    model.origin_B = Constraint(expr=model.x2 * 4 <= 12)

    result = SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model)
    result.write()
    print("\n****** Solution *******")
    print(f"profit = {model.profit()}")
    print(f"x1 = {model.x1()}, x2 = {model.x2()}")

    print("\n**** Sensitivity Analysis ****")
    print(f"y_equipment = {-model.dual[model.equipment]}")
    print(f"y_origin_A = {-model.dual[model.origin_A]}")
    print(f"y_origin_B = {-model.dual[model.origin_B]}")

    str = "   {0:7.2f} {1:7.2f} {2:7.2f} {3:7.2f}"

    print("Constraint  value  lslack  uslack    dual")
    for c in [model.equipment, model.origin_A, model.origin_B]:
        print(c, str.format(c(), c.lslack(), c.uslack(), model.dual[c]))


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


def exp3():
    """
     page 94 例1

     三个加工厂A1 A2 A3, 生产量7， 4， 9
     四个销售点B1, B2, B3, B4， 需求3，6，5，6
     单位运价：
            B1  B2  B3  B4
     A1     3   11  3   10
     A2     1   9   2   8
     A3     7   4   10  5
     求运费最小值？
    """
    factory = {"A1": 7, "A2": 4, "A3": 9}
    market = {"B1": 3, "B2": 6, "B3": 5, "B4": 6}
    cost_price = {
        ("A1", "B1"): 3,
        ("A1", "B2"): 11,
        ("A1", "B3"): 3,
        ("A1", "B4"): 10,
        ("A2", "B1"): 1,
        ("A2", "B2"): 9,
        ("A2", "B3"): 2,
        ("A2", "B4"): 8,
        ("A3", "B1"): 7,
        ("A3", "B2"): 4,
        ("A3", "B3"): 10,
        ("A3", "B4"): 5,
    }
    df = pd.DataFrame(0, index=factory, columns=market)
    for (x, y), v in cost_price.items():
        df.loc[x, y] = v
    print(df)

    model = ConcreteModel()

    model.x = Var(factory, market, domain=NonNegativeReals)

    model.cost = Objective(expr=sum(model.x[x, y] * cost_price[(x, y)] for x in factory for y in market),
                           sense=minimize)

    model.supply = ConstraintList()
    for f, v in factory.items():
        model.supply.add(expr=sum(model.x[f, m] for m in market) >= v)
    model.demand = ConstraintList()
    for m, v in market.items():
        model.demand.add(expr=sum(model.x[f, m] for f in factory) == v)

    result = SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model)
    print("\n==Solution==")
    print(f"min cost = {model.cost()}")
    df = pd.DataFrame(0, index=factory, columns=market)
    for x, y in cost_price:
        df.loc[x, y] = model.x[x, y]()
    print(df)


if __name__ == '__main__':
    exp3()
