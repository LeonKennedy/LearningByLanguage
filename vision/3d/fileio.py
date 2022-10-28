#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: fileio.py
@time: 2022/10/28 15:24
@desc:
"""
import open3d as o3d
import numpy as np

filename = "color_cube.ply"
# filename = "cube.ply.ply"
pcd = o3d.io.read_triangle_mesh(filename)
o3d.visualization.draw_geometries([pcd])
# o3d.visualization.draw_geometries([pcd],
#                                   zoom=0.7,
#                                   front=[0.5439, -0.2333, -0.8060],
#                                   lookat=[2.4615, 2.1331, 1.338],
#                                   up=[-0.1781, -0.9708, 0.1608])