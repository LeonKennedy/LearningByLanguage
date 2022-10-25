#!/usr/bin/env python
# encoding: utf-8

import pyomo.environ as pye
from pyomo.environ import ConstraintList, Var, NonNegativeIntegers, NonNegativeReals, Objective, minimize
import numpy as np

M = pye.ConcreteModel()
# var
m = 6  # j
n = 4  # i
t = [0.45, 0.02, 0, 0, 0, 0]
k = [1, 1, 0, 0, 0, 0]
e = [
    0.2887, 0.0149, 0.1018, 0.0068, 0.233, 0.0011,
    0.3660, 0.0096, 0.0829, 0.0027, 0.1141, 0.0022,
    0.5107, 0.0095, 0.0069, 0.0015, 0.0401, 0.0009,
    0.52, 0.0057, 0.013, 0.0017, 0.0289, 0.0014
]
e = np.array(e).reshape(4, 6).T
p = [10000, 100, 1, 1]
q = [0, 0, 0, 0]
lc = [340, 340, 340, 340]
t_board = [
    [0.45, 1],
    [0, 0.02],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1]
]

Q_0 = 1
h_0 = 1

# object
x_key = list(range(n))
M.x = Var(x_key, domain=NonNegativeReals)
M.obj = Objective(
    expr=pow(10, 8) * sum(
        k[j] * pow(sum([M.x[i] * e[j, i] / Q_0 - t[j] for i in range(n)]), 2) for j in range(m)) + sum(
        p[i] * pow(M.x[i] / h_0 - lc[i], 2) for i in range(n)),
    sense=minimize)

# constract
M.c1 = ConstraintList()
for i in x_key:
    M.c1.add(expr=M.x[i] <= lc[i] * h_0)
    M.c1.add(expr=M.x[i] >= q[i])
M.c2 = pye.Constraint(expr=sum(M.x[i] for i in x_key) <= Q_0)
M.c3 = pye.Constraint(expr=sum(M.x[i] for i in x_key) >= Q_0 * 0.85)

M.c4 = ConstraintList()
for j in range(n):
    M.c4.add(expr=sum(M.x[i] * e[j, i] / Q_0 for i in range(n)) <= t_board[j][1])
    M.c4.add(expr=sum(M.x[i] * e[j, i] / Q_0 for i in range(n)) >= t_board[j][0])


# solve

def solve(M):
    print("---- Solving -----")
    # opt = pye.SolverFactory('glpk', executable='/usr/local/bin/glpsol', name="Transfer Mission Assignment")
    opt = pye.SolverFactory('ipopt', name="Transfer Mission Assignment")
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


if solve(M):
    for i in range(n):
        print(f"x {i}:", M.x[i]())
