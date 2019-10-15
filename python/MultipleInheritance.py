#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: MultipleInheritance.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-10-14 16:14
# @Last Modified: 2019-10-14 16:14


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        # super().__init__(length, length)
        super(Square, self).__init__(length, length)


class Cube(Square):
    def surface_area(self):
        # face_area = super().area()
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        # face_area = super().area()
        face_area = super(Square, self).area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


if __name__ == '__main__':
    r = RightPyramid(2, 3)
