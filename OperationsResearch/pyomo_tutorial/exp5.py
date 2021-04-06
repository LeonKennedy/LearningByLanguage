#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp5.py.py
@time: 2021/3/30 4:15 下午
@desc:
https://jckantor.github.io/ND-Pyomo-Cookbook/02.05-Gasoline-Blending.html
"""

from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, maximize, Constraint, Suffix, ConstraintList
from utils import solve
products = {
    'Regular': {'price': 2.75, 'octane': 87, 'RVPmin': 0.0, 'RVPmax': 15.0, 'benzene': 1.1},
    'Premium': {'price': 2.85, 'octane': 91, 'RVPmin': 0.0, 'RVPmax': 15.0, 'benzene': 1.1},
}

streams = {
    'Butane'      : {'RON': 93.0, 'MON': 92.0, 'RVP': 54.0, 'benzene': 0.00, 'cost': 0.85, 'avail': 30000},
    'LSR'         : {'RON': 78.0, 'MON': 76.0, 'RVP': 11.2, 'benzene': 0.73, 'cost': 2.05, 'avail': 35000},
    'Isomerate'   : {'RON': 83.0, 'MON': 81.1, 'RVP': 13.5, 'benzene': 0.00, 'cost': 2.20, 'avail': 0},
    'Reformate'   : {'RON': 100.0, 'MON': 88.2, 'RVP': 3.2, 'benzene': 1.85, 'cost': 2.80, 'avail': 60000},
    'Reformate LB': {'RON': 93.7, 'MON': 84.0, 'RVP': 2.8, 'benzene': 0.12, 'cost': 2.75, 'avail': 0},
    'FCC Naphtha' : {'RON': 92.1, 'MON': 77.1, 'RVP': 1.4, 'benzene': 1.06, 'cost': 2.60, 'avail': 70000},
    'Alkylate'    : {'RON': 97.3, 'MON': 95.9, 'RVP': 4.6, 'benzene': 0.00, 'cost': 2.75, 'avail': 40000},
}


# calculate road octane as (R+M)/2
for s in streams.keys():
    streams[s]['octane'] = (streams[s]['RON'] + streams[s]['MON'])/2

# create model
m = ConcreteModel()

# create decision variables
S = streams.keys()
P = products.keys()
m.x = Var(S,P, domain=NonNegativeReals)

revenue = sum(sum(m.x[s,p]*products[p]['price'] for s in S) for p in P)
cost = sum(sum(m.x[s,p]*streams[s]['cost'] for s in S) for p in P)
m.profit = Objective(expr = revenue - cost, sense=maximize)

# constraints
m.cons = ConstraintList()
for s in S:
    m.cons.add(sum(m.x[s,p] for p in P) <= streams[s]['avail'])
for p in P:
    m.cons.add(sum(m.x[s,p]*(streams[s]['octane'] -    products[p]['octane'])       for s in S) >= 0)
    m.cons.add(sum(m.x[s,p]*(streams[s]['RVP']**1.25 - products[p]['RVPmin']**1.25) for s in S) >= 0)
    m.cons.add(sum(m.x[s,p]*(streams[s]['RVP']**1.25 - products[p]['RVPmax']**1.25) for s in S) <= 0)
    m.cons.add(sum(m.x[s,p]*(streams[s]['benzene'] -   products[p]['benzene'])      for s in S) <= 0)

solve(m)

# display results
vol = sum(m.x[s,p]() for s in S for p in P)
print("Total Volume =", round(vol, 1), "gallons.")
print("Total Profit =", round(m.profit(), 1), "dollars.")
print("Profit =", round(100*m.profit()/vol,1), "cents per gallon.")