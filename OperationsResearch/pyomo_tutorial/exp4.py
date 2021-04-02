#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: exp4.py
@time: 2021/3/29 5:57 下午
@desc:
https://jckantor.github.io/ND-Pyomo-Cookbook/02.04-Mixture-Design-Cold-Weather-Fuel.html
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, maximize, Constraint, Suffix, ConstraintList
from utils import solve

data = {
    'ethanol': {'MW': 46.07, 'SG': 0.791, 'A': 8.04494, 'B': 1554.3, 'C': 222.65},
    'methanol': {'MW': 32.04, 'SG': 0.791, 'A': 7.89750, 'B': 1474.08, 'C': 229.13},
    'isopropyl alcohol': {'MW': 60.10, 'SG': 0.785, 'A': 8.11778, 'B': 1580.92, 'C': 219.61},
    'acetone': {'MW': 58.08, 'SG': 0.787, 'A': 7.02447, 'B': 1161.0, 'C': 224.0},
    'xylene': {'MW': 106.16, 'SG': 0.870, 'A': 6.99052, 'B': 1453.43, 'C': 215.31},
    'toluene': {'MW': 92.14, 'SG': 0.865, 'A': 6.95464, 'B': 1344.8, 'C': 219.48},
}


# log_{10}P^{vap}_{s}(T) & = A_s - \frac{B_s}{T + C_s}
def Pvap(T, s):
    return 10 ** (data[s]['A'] - data[s]['B'] / (T + data[s]['C']))


def Pvap_denatured(T):
    return 0.4 * Pvap(T, 'ethanol') + 0.6 * Pvap(T, 'methanol')


T = np.linspace(0, 40, 200)

for s in data.keys():
    plt.plot(T, Pvap(T, s))
plt.plot(T, Pvap_denatured(T), 'k', lw=3)
plt.legend(list(data.keys()) + ['denatured alcohol'])
plt.title('Vapor Pressure of selected compounds')
plt.xlabel('temperature / °C')
plt.ylabel('pressure / mmHg')
plt.grid(True)
plt.show()

m = ConcreteModel()

S = data.keys()
m.x = Var(S, domain=NonNegativeReals)


def Pmix(T):
    return sum(m.x[s] * Pvap(T, s) for s in S)


m.obj = Objective(expr=Pmix(-10), sense=maximize)

m.cons = ConstraintList()
m.cons.add(sum(m.x[s] for s in S) == 1)
m.cons.add(Pmix(30) <= Pvap_denatured(30))
m.cons.add(Pmix(40) <= Pvap_denatured(40))
solve(m)

print("Vapor Pressure at -10°C =", m.obj(), "mmHg")

T = np.linspace(-10, 40, 200)
plt.plot(T, Pvap_denatured(T), 'k', lw=3)
plt.plot(T, [Pmix(T)() for T in T], 'r', lw=3)
plt.legend(['denatured alcohol'] + ['cold weather blend'])
plt.title('Vapor Pressure of selected compounds')
plt.xlabel('temperature / °C')
plt.ylabel('pressure / mmHg')
plt.grid(True)
plt.show()

results = pd.DataFrame.from_dict(data).T
for s in S:
    results.loc[s, 'mole fraction'] = m.x[s]()

MW = sum(m.x[s]() * data[s]['MW'] for s in S)
for s in S:
    results.loc[s, 'mass fraction'] = m.x[s]() * data[s]['MW'] / MW

vol = sum(m.x[s]() * data[s]['MW'] / data[s]['SG'] for s in S)
for s in S:
    results.loc[s, 'vol fraction'] = m.x[s]() * data[s]['MW'] / data[s]['SG'] / vol

print(results)