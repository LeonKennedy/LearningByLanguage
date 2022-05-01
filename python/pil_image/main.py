#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: main.py
@time: 2022/5/1 13:20
@desc:
"""
from PIL import Image
from tempfile import SpooledTemporaryFile, TemporaryFile, NamedTemporaryFile
import os
from shutil import copyfile


def run():
    img = Image.open("test.jpg")
    img.save("test_copy.jpg")
    with NamedTemporaryFile() as f:
        img.save(f, format=img.format)
        print(f.name)
        copyfile(f.name, "test_copyfile.jpg")

        img2 = Image.open(f)
        assert img2.width == img.width



if __name__ == '__main__':
    run()
