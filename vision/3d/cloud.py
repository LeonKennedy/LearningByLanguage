import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt


# print(np.asarray(pcd.points))

def _get_ply_point_cloud():
    ply_point_cloud = o3d.data.PLYPointCloud()
    pcd = o3d.io.read_point_cloud(ply_point_cloud.path)
    # print(pcd)
    return pcd


# 1
def cloud():
    pcd = _get_ply_point_cloud()
    o3d.visualization.draw_geometries([pcd],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


# 2
def donwsampling():
    pcd = _get_ply_point_cloud()
    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    o3d.visualization.draw_geometries([downpcd],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


# 3
def estimate_normals():
    pcd = _get_ply_point_cloud()
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    print("Recompute the normal of the downsampled point cloud")
    downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    o3d.visualization.draw_geometries([downpcd],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024],
                                      point_show_normal=True)


def _get_chair_point_cloud():
    demo_crop_data = o3d.data.DemoCropPointCloud()
    pcd = o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)
    vol = o3d.visualization.read_selection_polygon_volume(demo_crop_data.cropped_json_path)
    chair = vol.crop_point_cloud(pcd)
    return chair


# 4
def corp():
    chair = _get_chair_point_cloud()
    chair.paint_uniform_color([1, 0.706, 0])
    o3d.visualization.draw_geometries([chair],
                                      zoom=0.7,
                                      front=[0.5439, -0.2333, -0.8060],
                                      lookat=[2.4615, 2.1331, 1.338],
                                      up=[-0.1781, -0.9708, 0.1608])


# 5
def distance():
    demo_crop_data = o3d.data.DemoCropPointCloud()
    pcd = o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)
    vol = o3d.visualization.read_selection_polygon_volume(demo_crop_data.cropped_json_path)
    chair = vol.crop_point_cloud(pcd)

    dists = pcd.compute_point_cloud_distance(chair)
    dists = np.asarray(dists)
    ind = np.where(dists > 0.01)[0]
    pcd_without_chair = pcd.select_by_index(ind)
    o3d.visualization.draw_geometries([pcd_without_chair],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])


def bounding_volumes():
    chair = _get_chair_point_cloud()
    aabb = chair.get_axis_aligned_bounding_box()
    aabb.color = (1, 0, 0)
    obb = chair.get_oriented_bounding_box()
    obb.color = (0, 1, 0)
    o3d.visualization.draw_geometries([chair, aabb, obb],
                                      zoom=0.7,
                                      front=[0.5439, -0.2333, -0.8060],
                                      lookat=[2.4615, 2.1331, 1.338],
                                      up=[-0.1781, -0.9708, 0.1608])


def convex_hull():
    bunny = o3d.data.BunnyMesh()
    mesh = o3d.io.read_triangle_mesh(bunny.path)
    mesh.compute_vertex_normals()

    pcl = mesh.sample_points_poisson_disk(number_of_points=2000)
    hull, _ = pcl.compute_convex_hull()
    hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
    hull_ls.paint_uniform_color((1, 0, 0))
    o3d.visualization.draw_geometries([pcl, hull_ls])


def dbscan_clustering():
    ply_point_cloud = o3d.data.PLYPointCloud()
    pcd = o3d.io.read_point_cloud(ply_point_cloud.path)

    with o3d.utility.VerbosityContextManager(
            o3d.utility.VerbosityLevel.Debug) as cm:
        labels = np.array(
            pcd.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))

    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcd],
                                      zoom=0.455,
                                      front=[-0.4999, -0.1659, -0.8499],
                                      lookat=[2.1813, 2.0619, 2.0999],
                                      up=[0.1204, -0.9852, 0.1215])


def plane_segmentation():
    pcd_point_cloud = o3d.data.PCDPointCloud()
    pcd = o3d.io.read_point_cloud(pcd_point_cloud.path)
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                             ransac_n=3,
                                             num_iterations=1000)
    [a, b, c, d] = plane_model
    print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

    inlier_cloud = pcd.select_by_index(inliers)
    inlier_cloud.paint_uniform_color([1.0, 0, 0])
    outlier_cloud = pcd.select_by_index(inliers, invert=True)
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
                                      zoom=0.8,
                                      front=[-0.4999, -0.1659, -0.8499],
                                      lookat=[2.1813, 2.0619, 2.0999],
                                      up=[0.1204, -0.9852, 0.1215])


if __name__ == '__main__':
    plane_segmentation()
