#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: mesh.py
@time: 2022/10/28 16:19
@desc:
"""
import open3d as o3d
import numpy as np


def mm():
    print("Testing mesh in Open3D...")
    # armadillo_mesh = o3d.data.ArmadilloMesh()
    # mesh = o3d.io.read_triangle_mesh(armadillo_mesh.path)

    knot_mesh = o3d.data.KnotMesh()
    mesh = o3d.io.read_triangle_mesh(knot_mesh.path)
    mesh.compute_vertex_normals()
    print(mesh.triangles)
    # print(mesh)
    # print('Vertices:')
    # print(np.asarray(mesh.vertices))
    # print('Triangles:')
    # print(np.asarray(mesh.triangles))
    #
    # print("Try to render a mesh with normals (exist: " +
    #       str(mesh.has_vertex_normals()) + ") and colors (exist: " +
    #       str(mesh.has_vertex_colors()) + ")")
    # o3d.visualization.draw_geometries([mesh])
    # print("A mesh with no normals and no colors does not look good.")

if __name__ == '__main__':
    mm()
