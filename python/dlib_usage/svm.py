#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: example1.py
@time: 2022/11/8 17:40
@desc: 使用dlib创建一个简答的二分类SVM
"""

import dlib

try:
    import cPickle as pickle
except ImportError:
    import pickle

x = dlib.vectors()
y = dlib.array()

x.append(dlib.vector([1, 2, 3, -1, -2, -3]))
y.append(+1)

x.append(dlib.vector([-1, -2, -3, 1, 2, 3]))
y.append(-1)

#  svm = dlib.svm_c_trainer_histogram_intersection()
#  svm = dlib.svm_c_trainer_radial_basis()
svm = dlib.svm_c_trainer_linear()
svm.be_verbose()
svm.set_c(10)

classifier = svm.train(x, y)

print("prediction for first sample:  {}".format(classifier(x[0])))
print("prediction for second sample: {}".format(classifier(x[1])))

with open('saved_model.pickle', 'wb') as handle:
    pickle.dump(classifier, handle, 2)
