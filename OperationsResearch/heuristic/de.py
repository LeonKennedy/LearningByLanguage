#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: de.py
@time: 2021/4/15 11:54 上午
@desc:
"""

from sko.DE import DE
from sko.GA import GA
import pandas as pd
import numpy as np


def exp1():
    '''
    min f(x1, x2, x3) = x1^2 + x2^2 + x3^2
    s.t.
        x1*x2 >= 1
        x1*x2 <= 5
        x2 + x3 = 1
        0 <= x1, x2, x3 <= 5
    '''
    constraint_eq = [
        lambda x: 1 - x[1] - x[2]
    ]
    constraint_ueq = [
        lambda x: 1 - x[0] * x[1],
        lambda x: x[0] * x[1] - 5
    ]
    de = DE(func=lambda p: sum(i ** 2 for i in p), n_dim=3, size_pop=50, max_iter=800, lb=[0, 0, 0], ub=[5, 5, 5],
            constraint_eq=constraint_eq, constraint_ueq=constraint_ueq)

    best_x, best_y = de.run()
    print('best_x:', best_x, '\n', 'best_y:', best_y)


class ZeroOneDe(GA):
    def crtbp(self):
        # create the population
        self.Chrom = np.zeros((self.size_pop, self.len_chrom), dtype=np.int8)
        spell = list(range(0, self.len_chrom, 4))
        for i in range(self.size_pop):
            for j in spell:
                self.Chrom[i, np.random.randint(j, j + 4)] = 1
        return self.Chrom

    # def mutation(self):
    #     for i in range(self.size_pop):
    #         self.Chrom[i, np.random.randint(0, 2)] ^= 1


def exp2():
    data = {"英": [2, 10, 9, 7], "日": [15, 4, 14, 8], "德": [13, 14, 16, 11], "俄": [4, 15, 13, 9]}
    df = pd.DataFrame(data, index=["甲", "乙", "丙", "丁"])
    print(df)
    ser = df.stack().to_numpy()

    def objective(p):
        return np.sum(p * ser)

    constraint_eq = []
    constraint_eq.append(lambda x: x[0] + x[1] + x[2] + x[3] - 1)
    constraint_eq.append(lambda x: x[4] + x[5] + x[6] + x[7] - 1)
    constraint_eq.append(lambda x: x[8] + x[9] + x[10] + x[11] - 1)
    constraint_eq.append(lambda x: x[12] + x[13] + x[14] + x[15] - 1)

    constraint_eq.append(lambda x: x[0] + x[4] + x[8] + x[12] - 1)
    constraint_eq.append(lambda x: x[1] + x[5] + x[9] + x[13] - 1)
    constraint_eq.append(lambda x: x[2] + x[6] + x[10] + x[14] - 1)
    constraint_eq.append(lambda x: x[3] + x[7] + x[11] + x[15] - 1)
    # for i in range(4):
    #     print(list(range(i, len(ser), 4)))
    #     constraint_eq.append(lambda x: sum(x[j] for j in range(i, len(ser), 4)) - 1)
    #
    # for i in range(0, len(ser), 4):
    #     print(list(range(i, i + 4)))
    #     constraint_eq.append(lambda x: sum(x[j] for j in range(i, i + 4)) - 1)

    # de = GA(func=objective, n_dim=len(ser), size_pop=100, max_iter=100, lb=0, ub=1,
    #                precision=1, constraint_eq=constraint_eq)
    de = DE(func=objective, n_dim=len(ser), size_pop=100, max_iter=100, lb=0, ub=1,
            constraint_eq=constraint_eq)

    return de, ser


if __name__ == '__main__':
    de, ser = exp2()
    best_x, best_y = de.run()

    print('best_x:', best_x, '\n', 'best_y:', best_y)
