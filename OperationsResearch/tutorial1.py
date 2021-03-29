#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: tutorial1.py
@time: 2021/3/29 2:03 下午
@desc:
"""

import random
import docplex.mp.model as cpx
import pandas as pd

n = 10
m = 5
set_I = range(1, n + 1)
set_J = range(1, m + 1)
c = {(i, j): random.normalvariate(0, 1) for i in set_I for j in set_J}
a = {(i, j): random.normalvariate(0, 5) for i in set_I for j in set_J}
l = {(i, j): random.randint(0, 10) for i in set_I for j in set_J}
u = {(i, j): random.randint(10, 20) for i in set_I for j in set_J}
b = {j: random.randint(0, 30) for j in set_J}

opt_model = cpx.Model(name="MIP Model")

# x is continuous
x_vars = {(i, j): opt_model.continuous_var(lb=l[i, j], ub=u[i, j], name=f"x_{i}_{j}") for i in set_I for j in set_J}
# if x is Binary
# x_vars = {(i, j): opt_model.binary_var(name=f"x_{i}_{j}") for i in set_I for j in set_J}
# if x is Integer
# x_vars = {(i, j): opt_model.integer_var(lb=l[i, j], ub=u[i, j], name=f"x_{i}_{j}") for i in set_I for j in set_J}


# >= constraints
constraints = {j: opt_model.add_constraint(ct=opt_model.sum(a[i, j] * x_vars[i, j] for i in set_I) <= b[j],
                                           ctname=f"constraint_{j}")
               for j in set_J}

objective = opt_model.sum(x_vars[i, j] * c[i, j]
                          for i in set_I
                          for j in set_J)

opt_model.maximize(objective)
# opt_model.minimize(objective)

opt_model.solve()

opt_df = pd.DataFrame.from_dict(x_vars, orient="index",  columns=["variable_object"])
opt_df.index = pd.MultiIndex.from_tuples(opt_df.index, names=["column_i", "column_j"])
opt_df.reset_index(inplace=True)

# CPLEX
opt_df["solution_value"] = opt_df["variable_object"].apply(lambda item: item.solution_value)

opt_df.drop(columns=["variable_object"], inplace=True)
opt_df.to_csv("./optimization_solution.csv")
