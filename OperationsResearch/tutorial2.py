#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: tutorial2.py
@time: 2021/3/29 3:36 下午
@desc:
"""

from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, maximize, Constraint, SolverFactory

model = ConcreteModel()

model.x = Var(domain=NonNegativeReals)  # NonNegativeReals代表非0实数
model.y = Var(domain=NonNegativeReals)

# declare objective
model.profit = Objective(expr=40 * model.x + 30 * model.y, sense=maximize)

# declare constraints
model.demand = Constraint(expr=model.x <= 40)
model.laborA = Constraint(expr=model.x + model.y <= 80)
model.laborB = Constraint(expr=2 * model.x + model.y <= 100)
model.pprint()

SolverFactory('glpk', executable='/usr/local/bin/glpsol').solve(model).write()

# display solution
print('\nProfit = ', model.profit())


print('\nDecision Variables')
print('x = ', model.x())
print('y = ', model.y())


print('\nConstraints')
print('Demand  = ', model.demand())
print('Labor A = ', model.laborA())
print('Labor B = ', model.laborB())