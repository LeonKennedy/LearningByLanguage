#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: fit_hourse_price.py
@time: 2020/10/9 4:50 下午
@desc:
"""

import numpy as np


def preprocess(ratio=0.8):
    data = np.fromfile('housing.data', sep=' ')
    feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                     'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    feature_num = len(feature_names)
    data = data.reshape([data.shape[0] // feature_num, feature_num])
    print(f"data shape: {data.shape}")
    # split train and test
    data = normalize(data)

    offset = int(data.shape[0] * ratio)
    return data[:offset], data[offset:]


def normalize(data):
    maximum, minimum = data.max(axis=0), data.min(axis=0)
    return (data - minimum) / (maximum - minimum)


class Densen:
    def __init__(self, node_num=10, weight_num=13):
        self.weights = np.random.randn(node_num, weight_num)
        self.bias = np.random.randn(node_num)
        self.w = np.random.randn(node_num, 1)
        self.b = 0.

    def forward(self, x):
        self.layer_z = self.forward_layer(x)
        self.layer_a = self.activate(self.layer_z)
        self.z = self.forward_output(self.layer_a)
        return self.z

    def forward_layer(self, x):
        """

        :param x:
        :return:  (404 * 10)
        """
        return np.dot(x, self.weights.T) + self.bias

    def forward_output(self, x):
        """

        :param x:
        :return: (404 * 1)
        """
        return np.dot(x, self.w) + self.b

    def activate(self, x):
        return 1 / (1 + np.exp(-x))

    def d_activate(self, x):
        sigmod = 1 / (1 + np.exp(-x))
        return (1 - sigmod) * sigmod

    def loss(self, z, y):
        error = z - y
        return np.square(error).mean()

    def round_L_z(self, y):
        """

        :param y:
        :return:  (N *  1)
        """
        return self.z - y

    def round_L_zi(self, y):
        """
            (N * 10) * (N * 10)
        :param y:
        :return:  (N * 10)
        """
        round_L_a = self.round_L_z(y) * self.w.T
        return self.layer_z * round_L_a

    def gradient_output(self, x, y):
        round_L_z = self.round_L_z(y)
        gradient_w = (round_L_z * x).mean(axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        gradient_b = round_L_z.mean(axis=0)
        return gradient_w, gradient_b

    def gradient_layer(self, x, y):
        round_L_zi = self.round_L_zi(y)
        gradient_bias = round_L_zi.mean(axis=0)
        round_L_zi = round_L_zi[:, np.newaxis, :]
        new_x = x[:, :, np.newaxis]
        t1 = round_L_zi * new_x
        gradient_weight = t1.mean(axis=0)
        return gradient_weight, gradient_bias

    def gradient(self, x, y):
        self.layer_z = self.forward_layer(x)
        self.layer_a = self.activate(self.layer_z)
        self.z = self.forward_output(self.layer_a)
        loss = self.loss(self.z, y)
        gradient_w, gradient_b = self.gradient_output(self.layer_a, y)
        gradient_weight, gradient_bias = self.gradient_layer(x, y)

        return gradient_w, gradient_b, gradient_weight, gradient_bias, loss

    def update(self, gw, gb, gweight, gbias, lr=0.01):
        self.w = self.w - lr * gw
        self.b = self.b - lr * gb
        self.weights = self.weights - lr * gweight.T
        self.bias = self.bias - lr * gbias

    def train(self, data, batch=77, epoch=999, lr=0.01):
        length = data.shape[0]
        for i in range(epoch):
            np.random.shuffle(data)
            mini_batches = [data[k:k + batch] for k in range(0, length, batch)]
            for iter, mini_batch in enumerate(mini_batches):
                x = mini_batch[:, :-1]
                y = mini_batch[:, -1:]
                gw, gb, gweight, gbias, loss = self.gradient(x, y)
                print(f"epoch: {i} iter: {iter} loss: {loss}")
                self.update(gw, gb, gweight, gbias, lr)
        print(f"iter: {i} loss: {loss}")

    def evaluation(self, data):
        x = data[:, :-1]
        y = data[:, -1:]
        z = self.forward(x)
        l = self.loss(z, y)
        print(f"test loss: {l}")


if __name__ == '__main__':
    train_data, test_data = preprocess()
    x = train_data[:, :-1]
    y = train_data[:, -1:]
    net = Densen(10, x.shape[1])
    net.train(train_data)
    net.evaluation(test_data)
