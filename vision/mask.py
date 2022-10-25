#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: mask.py.py
@time: 2022/10/25 10:18
@desc:
"""
import cv2
import numpy as np

img = cv2.imread("IMG_2958.JPG")


def bitwise_and():
    mask = np.zeros(img.shape, np.uint8)
    mask[250:350, :, :] = 255
    mask[:, 250:340, :] = 255
    img2 = cv2.bitwise_and(img, mask)
    cv2.imshow("corss", img2)


def run():
    bitwise_and()
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
