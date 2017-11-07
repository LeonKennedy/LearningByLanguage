#!/usr/bin/python

import math
import numpy as np
from sklearn import datasets
import pdb


def createDataSet():
    dataSet = datasets.load_iris()
    iris_X = dataSet.data
    iris_y = dataSet.target
    np.random.seed(1)
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test  = iris_X[indices[-10:]]
    iris_y_test  = iris_y[indices[-10:]]
    dataSet = datasets.load_iris()
    return iris_X_train, iris_y_train, iris_X_test, iris_y_test

class Node:
    label = None
    gini = 1
    index = None
    isleaf = False
    label = None
    childrens = list()


    def predict(self, data):
        results = []
        for i in data:
            results.append(self.spredict(i))
        return np.array(results)

    def spredict(self, row):
        if self.isleaf:
            return self.label
        else:
            if row[0] <= self.index:
                return self.childrens[0].spredict(row[1:])
            else:
                return self.childrens[1].spredict(row[1:])

    def printself(self):
        if self.isleaf:
            print('gini: %f, index: %s, label %s, isleaf: %r' % (self.gini, self.index, self.label, self.isleaf))
        else:
            print('gini: %f, index: %s, label %s, isleaf: %r' % (self.gini, self.index, self.label, self.isleaf))
            print('=========')
            self.childrens[0].printself()
            self.childrens[1].printself()


class DecisionTree:
    
    root = None
    targetSize = 0

    def __init__(self, data, target):
        self.targetSize = np.unique(target).size

    #节点最佳划分度量是根据子女的不纯性
    def entropy(self, data):
        total = sum(data)
        return sum([ - (d/total) * math.log(d/total) / math.log(2) for d in data if d != 0])

    def gini(self, data):
        t  = data.sum()
        return 1 - sum([ pow(d/t, 2) for d in data])

    #----
    def createNode(self):
        return Node()

    def setsDifferentSets(self, x):
        ux = np.unique(x)
        ux.sort()
        return (ux[1:]-ux[:-1]) / 2 + ux[:-1]

    def wgini(self, table):
        total = table.sum()
        return sum([ row.sum()/total * self.gini(row) for row in table])

    def getGini(self, x, y):
        middleSets = self.setsDifferentSets(np.copy(x))
        target = np.unique(y)
        mingini = 1
        bestIndex = 0
        for i in middleSets:
            #TODO y.type.size
            table = np.zeros((2, self.targetSize))
            gtx = x >= i
            x2y = y[gtx]
            for oy in x2y:
                table[0,oy] += 1
            ltx = x < i
            x2y = y[ltx]
            for oy in x2y:
                table[1, oy] += 1
            if self.wgini(table) < mingini:
                mingini = self.wgini(table)
                bestIndex = i
        return mingini, bestIndex
        
    def findBestSplit(self, x, y):
        index = -1;
        m,n = x.shape
        for i in range(n):
            column = np.copy(x[:,i])
            self.getGini(column, y)
        return -1;

    def stopCondition(self, x, y):
        if np.unique(y).size == 1:
            return True
        if x.shape[1] == 0:
            return True
        return False
        
    def treeGrowth(self, x, y):
        if self.stopCondition(x,y) == True:
            leaf = self.createNode()
            leaf.isleaf = True
            bincount = np.bincount(y)
            leaf.label = np.argmax(bincount)
            return leaf
        else:
            x_data = x if len(x.shape) == 1 else x[:,0]
            gini,index = self.getGini(x_data, y)
            node = self.createNode()
            node.gini = gini
            node.index = index
            leftwhere = np.where(x_data <= index)[0]
            rightwhere = np.where(x_data > index)[0]
            l_x_rest, r_x_rest = (x[leftwhere, 1:], x[rightwhere, 1:])
            leftNode = self.treeGrowth(l_x_rest, y[leftwhere])
            rightNode = self.treeGrowth(r_x_rest, y[rightwhere])
            node.childrens = (leftNode, rightNode)
            return node

            
if __name__ == "__main__":
    x, y, xt, yt = createDataSet()
    a = DecisionTree(x,y)
    #a.getGini(x[:,3],y)
    #print(a.findBestSplit(x,y))
    a.root = a.treeGrowth(x,y)
    #a.root.printself()
    result = a.root.predict(xt)
    print('preidct:')
    print(result)
    print('target:')
    print(yt)

