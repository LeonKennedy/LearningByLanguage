#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: Assignment.py
@time: 2021/4/13 3:53 下午
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

    def _cost_sum():
        return sum(df.loc[i] * M.x[i] for i in M.x)

    M.cost = pye.Objective(expr=_cost_sum())

    # M.mission = pye.ConstraintList()
    # for j in df.columns:
    #     M.mission.add(expr=sum(M.x[i, j] for i in df.index) == 1)
    M.mission = pye.Constraint(df.columns, rule=lambda m, j: sum(m.x[i, j] for i in df.index) == 1)
    M.person = pye.Constraint(df.index, rule=lambda m, i: sum(m.x[i, j] for j in df.columns) == 1)

    opt = pye.SolverFactory('glpk', executable='/usr/local/bin/glpsol', name="Transfer Mission Assignment")
    result = opt.solve(M, tee=True)

    out = pd.DataFrame(0, index=df.index, columns=df.columns)
    for i in M.x:
        out.loc[i] = pye.value(M.x[i])  # M.x[i]()
    print(out)
    print("cost: ", M.cost())


def exp2():
    data = {"英": [2, 10, 9, 7, 4], "日": [15, 4, 14, 8, 7], "德": [13, 14, 16, 11, 12], "俄": [4, 15, 13, 9, 11]}
    df = pd.DataFrame(data, index=["甲", "乙", "丙", "丁", "戊"])
    print(df, "\n")
    M = pye.ConcreteModel()
    M.x = pye.Var(df.index, df.columns, domain=pye.Binary, bounds=(0, 1))
    M.cost = pye.Objective(expr=sum(df.loc[i] * M.x[i] for i in M.x))
    M.mission = pye.Constraint(df.columns, rule=lambda m, j: sum(m.x[i, j] for i in df.index) == 1)
    M.person = pye.Constraint(df.index, rule=lambda m, i: sum(m.x[i, j] for j in df.columns) <= 1)

    excl_pairs = [("甲", "戊"), ("甲", "乙"), ("丙", "丁")]
    M.disj = Disjunction(excl_pairs, rule=lambda m, a, b: [sum(m.x[a, j] for j in df.columns) == 0,
                                                           sum(m.x[b, j] for j in df.columns) == 0])
    TransformationFactory('gdp.hull').apply_to(M)
    opt = pye.SolverFactory('glpk', executable='/usr/local/bin/glpsol', name="Transfer Mission Assignment")
    result = opt.solve(M, tee=True)
    out = pd.DataFrame(0, index=df.index, columns=df.columns)
    for i in M.x:
        out.loc[i] = pye.value(M.x[i])  # M.x[i]()
    print(out, "\n")
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
