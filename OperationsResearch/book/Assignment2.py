#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: Assignment2.py.py
@time: 2021/12/31 11:39 AM
@desc:
"""

import pyomo.environ as pye
import pandas as pd
from pyomo.core import TransformationFactory
from pyomo.gdp import Disjunction
from pyomo.opt import SolverStatus, TerminationCondition


def exp1():
    data = {"英": [2, 10, 9, 7], "日": [15, 4, 14, 8], "德": [13, 14, 16, 11], "俄": [4, 15, 13, 9]}
    df = pd.DataFrame(data, index=["甲", "乙", "丙", "丁"])
    print(df)

    M = pye.ConcreteModel()
    M.x = pye.Var(df.index, df.columns, domain=pye.Binary)
    # M.x['甲', '德'].fix(1)
    M.x['甲', '俄'].fix(0)

    M.cost = pye.Objective(expr=sum(df.loc[i] * M.x[i] for i in M.x))

    M.mission = pye.Constraint(df.columns, rule=lambda m, j: sum(m.x[i, j] for i in df.index) == 1)
    M.person = pye.Constraint(df.index, rule=lambda m, i: sum(m.x[i, j] for j in df.columns) == 1)

    opt = pye.SolverFactory('glpk', executable='/usr/local/bin/glpsol', name="Transfer Mission Assignment")
    result = opt.solve(M, tee=False)

    out = pd.DataFrame(0, index=df.index, columns=df.columns)
    for i in M.x:
        out.loc[i] = pye.value(M.x[i])  # M.x[i]()
    print(out)
    print("cost: ", M.cost())


def solve(M):
    opt = pye.SolverFactory('glpk', executable='/usr/local/bin/glpsol', name="Transfer Mission Assignment")
    results = opt.solve(M, tee=True)
    results.write()
    if (results.solver.status == SolverStatus.ok) and (
            results.solver.termination_condition == TerminationCondition.optimal):
        print("this is feasible and optimal")
        M.solutions.load_from(results)
        return True
    elif results.solver.termination_condition == TerminationCondition.infeasible:
        print("do something about it? or exit?")
        return False
    else:
        print(str(results.solver))
        raise Exception()


if __name__ == '__main__':
    exp1()
