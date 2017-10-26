#!/bin/bash

import re, math

class classifier:

    def __init__(self):
        self.fc = {}
        self.cc = {}
        self.getFeatures = self.getWords

    def getWords(self, doc):
        words = [s.lower() for s in re.split('\W+', doc) if len(s) > 2 and len(s) < 20]
        return dict([ (w, 1) for w in words])

    def incc(self, cat):
        self.cc.setdefault(cat, 0)
        self.cc[cat] += 1
    
    def incf(self, f, cat):
        self.fc.setdefault(f, {})
        self.fc[f].setdefault(cat, 0)
        self.fc[f][cat] += 1

    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0
    
    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0.0

    def totalcount(self):
        return sum(self.cc.values())

    def categories(self):
        return self.cc.keys()

    def fprob(self, f, cat):
        if self.catcount(cat) == 0:
            return 0
        return self.fcount(f, cat) / self.catcount(cat)

    def weightprob(self, f, cat, prf, weight=1.0, ap=0.5):
        basicprob=prf(f,cat)
        totals =  sum([self.fcount(f, c) for c in self.categories()])
        return ((weight * ap) + (totals * basicprob)) / (weight + totals)

    def train(self, item, cat):
        features = self.getFeatures(item)
        for f in features:
            self.incf(f, cat)
        self.incc(cat)

class naivebayes(classifier):
    def docprob(self, item, cat):
        features = self.getFeatures(item)
        p = 1
        for f in features:
            p *= self.weightprob(f, cat, self.fprob)
        return p

    def prob(self, item, cat):
        catprob = self.catcount(cat) / self.totalcount()
        return self.docprob(item, cat) * catprob

if __name__ == "__main__":
    cf = naivebayes();
    docs = (('Nobody owns the water.','good'),\
        ('the quick rabbit jumps fences', 'good'),\
        ('buy pharmaceuticals now', 'bad'), \
        ('make quick money at the online casino', 'bad'),\
        ('the quick brown fox jumps', 'good'))
    for i in docs:
        cf.train(*i)
    #print(cf.fprob('money', 'good'))
    #$print(cf.weightprob('money', 'good', cf.fprob))
    print(cf.prob('quick rabbit', 'good'))
    print(cf.prob('quick rabbit', 'bad'))
