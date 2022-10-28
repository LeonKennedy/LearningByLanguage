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
import copy

import open3d as o3d
import numpy as np


def _get_mesh() -> o3d.geometry.TriangleMesh:
    knot_mesh = o3d.data.KnotMesh()
    mesh = o3d.io.read_triangle_mesh(knot_mesh.path)
    mesh.compute_vertex_normals()
    return mesh


def mesh_normals():
    print("Testing mesh in Open3D...")
    # armadillo_mesh = o3d.data.ArmadilloMesh()
    # mesh = o3d.io.read_triangle_mesh(armadillo_mesh.path)
    mesh = _get_mesh()
    print(mesh.triangles)
    print(mesh)
    print('Vertices:')
    print(np.asarray(mesh.vertices))
    print('Triangles:')
    print(np.asarray(mesh.triangles))

    print("Try to render a mesh with normals (exist: " +
          str(mesh.has_vertex_normals()) + ") and colors (exist: " +
          str(mesh.has_vertex_colors()) + ")")
    o3d.visualization.draw_geometries([mesh])
    print("A mesh with no normals and no colors does not look good.")


def corp_mesh():
    mesh = _get_mesh()
    print("We make a partial mesh of only the first half triangles.")
    mesh1 = copy.deepcopy(mesh)
    mesh1.paint_uniform_color([1, 0.706, 0])
    mesh1.triangles = o3d.utility.Vector3iVector(
        np.asarray(mesh1.triangles)[:len(mesh1.triangles) // 2, :])
    mesh1.triangle_normals = o3d.utility.Vector3dVector(
        np.asarray(mesh1.triangle_normals)[:len(mesh1.triangle_normals) // 2, :])
    print(mesh1.triangles)
    o3d.visualization.draw_geometries([mesh1])


if __name__ == '__main__':
    corp_mesh()
