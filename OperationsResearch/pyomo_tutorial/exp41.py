#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp41.py
@time: 2021/3/31 10:39 上午
@desc: Disjunctive Programming
https://jckantor.github.io/ND-Pyomo-Cookbook/04.01-Introduction_to_Disjunctive_Programming.html
"""

import pandas as pd
from pyomo.environ import ConcreteModel, Set, Var, NonNegativeReals, Objective, minimize, Constraint, Boolean,ConstraintList, TransformationFactory
from pyomo.gdp import Disjunction
from utils import solve
# load data as dictionary of components
# component data consists of cost and composition
comp_data = {
    "A": {"cost": 2.0, "Vit A": 0.5, "Vit B": 0.2},
    "B": {"cost": 2.0, "Vit A": 0.4, "Vit B": 0.1},
    "C": {"cost": 5.0, "Vit A": 0.3, "Vit B": 0.3},
}

prod_req = {
    "Vit A": {"lb": 0.0, "ub": 0.4},
    "Vit B": {"lb": 0.2, "ub": 1.0},
}

excl_pairs = [("A", "B")]

m = ConcreteModel()

# define sets that will be used to index decision variables and constraints
# remember to use initialize keyword
m.comp = Set(initialize=comp_data.keys())
m.req = Set(initialize=prod_req.keys())
m.pairs = Set(initialize=excl_pairs)
# decision variables
m.x = Var(m.comp, domain=NonNegativeReals, bounds=(0, 1))
# m.x = Var(m.comp, domain=NonNegativeReals)
m.y = Var(m.pairs, domain=Boolean)
m.cost = Objective(expr=sum( m.x[c] * comp_data[c]['cost'] for c in m.comp), sense=minimize)

# structural constraints
m.massfraction = Constraint(expr=sum(m.x[c] for c in m.comp) == 1)

# composition constraints
m.lb = Constraint(m.req, rule=lambda m, r: sum(m.x[c]*comp_data[c][r] for c in m.comp) >= prod_req[r]["lb"])
m.ub = Constraint(m.req, rule=lambda m, r: sum(m.x[c]*comp_data[c][r] for c in m.comp) <= prod_req[r]["ub"])
# m.a_ub = Constraint(expr= sum(m.x[c] * comp_data[c]["Vit A"] for c in m.comp) <= prod_req["Vit A"]['ub'])
# m.a_lb = Constraint(expr= sum(m.x[c] * comp_data[c]["Vit A"] for c in m.comp) >= prod_req["Vit A"]['lb'])
# m.b_ub = Constraint(expr= sum(m.x[c] * comp_data[c]["Vit B"] for c in m.comp) <= prod_req["Vit B"]['ub'])
# m.b_lb = Constraint(expr= sum(m.x[c] * comp_data[c]["Vit B"] for c in m.comp) >= prod_req["Vit B"]['lb'])

# # component incompatability constraints
# M = 100
# m.disj = ConstraintList()
# for pair in m.pairs:
#     a, b = pair
#     m.disj.add(m.x[a] <= M*m.y[pair])
#     m.disj.add(m.x[b] <= M*(1-m.y[pair]))

# component incompatability constraints
m.disj = Disjunction(m.pairs, rule=lambda m, a, b: [m.x[a] == 0, m.x[b] == 0])

# apply transformations
TransformationFactory('gdp.hull').apply_to(m)

result = solve(m)
# result.write()

for c in m.comp:
    print(f"{c} = {m.x[c]()}")