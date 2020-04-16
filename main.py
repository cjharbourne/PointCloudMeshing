from pyntcloud import PyntCloud
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import BallTree
from stl import mesh

import lifted_triangulation as triangulate

## Input 3D point cloud using PyntCloud Library
wolf = PyntCloud.from_file("wolf.pcd")

#wolf.plot()

## Transfer pointcloud to a dataframe
arr = np.asarray(wolf.xyz)
wolf = None

## 1. Build BallTree
neighbors = BallTree(arr, metric='braycurtis')


## Build KD-Tree
dist, ind = neighbors.query(arr, k=15)

## Declare PCA model
pca = PCA(n_components = 2)

## Declare an array to store all the tiangles for the mesh
triangles = []

##  Iterate through each point
for i in range(len(arr)):
    print("loop {}".format(i))

    ## Build list of X - nearest points
    ## PCA reduce to 2D

    temp = pca.fit_transform(arr[ind[i]])
    ## Pass 2-D points to twoD.py
    ## Returns all triangles that touch the point arr[1]
    _triangles = triangulate.processing(temp)

    for tri in _triangles:
        temp = [ind[i][num] for num in tri]
        triangles.append([[item for item in arr[num]] for num in temp])

wolf = mesh.Mesh(np.zeros(np.shape(triangles)[0], dtype=mesh.Mesh.dtype))

for idx, face in enumerate(triangles):
    wolf.vectors[idx] = face

wolf.save('ball_wolf_braycurtis.stl')
print("Completed Final STL Generation")



































#
