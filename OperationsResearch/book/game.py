#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: game.py
@time: 2021/5/13 3:11 下午
@desc:
"""

import numpy as np
import pyomo.environ as pye


def main(matrix):
    print("payoff game matrix:")
    print(matrix)
    M = pye.ConcreteModel()
    M.dual = pye.Suffix(direction=pye.Suffix.IMPORT)
    index = list(range(matrix.shape[0]))
    M.x = pye.Var(index, domain=pye.NonNegativeReals)

    M.obj = pye.Objective(expr=sum(M.x[i] for i in index), sense=pye.minimize)
    M.con = pye.ConstraintList()
    for i in range(matrix.shape[1]):
        s = matrix[:, i]
        M.con.add(expr=sum(M.x[j] * v for j, v in enumerate(s)) >= 1)

    solve(M)
    print("--- output ----")
    print(f"x = {[M.x[i]() for i in M.x]}")
    print(f"v_x = {M.obj()}")
    print(f"y = {[M.dual[M.con[i]] for i in M.con]}")
    print(f"=====\n V_G = {1 / M.obj()}")


def solve(M):
    print("---- Solving -----")
    opt = pye.SolverFactory('glpk', executable='/usr/local/bin/glpsol', name="Transfer Mission Assignment")
    results = opt.solve(M, tee=False)
    # results.write()
    if (results.solver.status == pye.SolverStatus.ok) and (
            results.solver.termination_condition == pye.TerminationCondition.optimal):
        print("this is feasible and optimal")
        M.solutions.load_from(results)
        return True
    elif results.solver.termination_condition == pye.TerminationCondition.infeasible:
        print("do something about it? or exit?")
        return False
    else:
        print(str(results.solver))
        raise Exception()


if __name__ == '__main__':
    matrix = np.array([7, 2, 9, 2, 9, 0, 9, 0, 11]).reshape(3, 3)
    # matrix = np.array([8, 2, 4, 2, 6, 6, 6, 4, 4]).reshape(3, 3)
    # matrix = np.array([2, 0, 2, 0, 3, 1, 1, 2, 1]).reshape(3, 3)
    main(matrix)
