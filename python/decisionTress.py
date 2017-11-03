#!/usr/bin/python

import math
import numpy as np

class DecisionTree:
    

    #节点最佳划分度量是根据子女的不纯性
    def entropy(self, data):
        total = sum(data)
        return sum([ - (d/total) * math.log(d/total) / math.log(2) for d in data if d != 0])

    def gini(self, data):
        pass


if __name__ == "__main__":
    a = DecisionTree()
    d = (1,5)
    print(a.entropy(d))

