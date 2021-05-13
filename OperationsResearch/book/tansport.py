#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: tansport.py
@time: 2021/4/8 3:24 下午
@desc:
"""
from pyomo.environ import ConstraintList, ConcreteModel, Var, NonNegativeIntegers, NonNegativeReals, \
    Objective, SolverFactory, minimize
import pandas as pd


def exp1():
    fee = pd.DataFrame({'e': [16, 14, 19], 'f': [13, 13, 20], 'g': [22, 19, 23], 'h': [17, 15, 9999]},
                       index=['A', 'B', 'C'])
    supply = {"A": 50, "B": 60, "C": 50}
    demand = {'e': {'low': 30, 'up': 50},
              'f': 70,
              'g': {'low': 0, 'up': 30},
              'h': {'low': 10}
              }
    print(fee)

    m = ConcreteModel()
    valid_key = set((i, j) for i in supply for j in demand if not (i == "C" and j == "h"))
    m.x = Var(valid_key, domain=NonNegativeReals)

    m.cost = Objective(expr=sum(m.x[i, j] * fee.loc[i, j] for i, j in valid_key))

    m.supply = ConstraintList()
    for i, value in supply.items():
        m.supply.add(expr=sum(m.x[i, j] for j in demand if (i, j) in valid_key) <= value)

    m.demand = ConstraintList()
    for j, value in demand.items():
        if isinstance(value, dict):
            if 'low' in value:
                m.demand.add(expr=sum(m.x[i, j] for i in supply if (i, j) in valid_key) >= value['low'])
            if 'up' in value:
                m.demand.add(expr=sum(m.x[i, j] for i in supply if (i, j) in valid_key) <= value['up'])
        else:
            m.demand.add(expr=sum(m.x[i, j] for i in supply if (i, j) in valid_key) == value)

    result = SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(m)
    assert_optimal_termination(results)
    print("\n==Solution==")
    print(f"min cost = {m.cost()}")
    schedule = pd.DataFrame(0, index=fee.index, columns=fee.columns)
    for i, j in valid_key:
        schedule.loc[i, j] = m.x[i, j]()
    print(schedule)


def exp2():
    supply = {1: 25, 2: 35, 3: 30, 4: 10}
    supply_cost = {1: 10.8, 2: 11.1, 3: 11.0, 4: 11.3}
    persistence_cost = 0.15
    demand = {1: 10, 2: 15, 3: 25, 4: 20}

    m = ConcreteModel()
    valid_key = set()
    for i in supply:
        for j in demand:
            if i <= j:
                valid_key.add((i, j))

    m.x = Var(valid_key, domain=NonNegativeReals)

    def fee(i, j):
        return round(supply_cost[i] + (j - i) * persistence_cost, 2)

    m.cost = Objective(expr=sum(m.x[i, j] * fee(i, j) for i, j in valid_key))

    m.supply = ConstraintList()
    for i, value in supply.items():
        m.supply.add(expr=sum(m.x[i, j] for j in demand if (i, j) in valid_key) <= value)

    m.demand = ConstraintList()
    for j, value in demand.items():
        m.demand.add(expr=sum(m.x[i, j] for i in supply if i <= j) == value)

    result = SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(m)
    print("\n==Solution==")
    print(f"min cost = {m.cost()}")


if __name__ == '__main__':
    exp2()
