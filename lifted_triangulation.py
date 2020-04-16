import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import ConvexHull


def processing(points):
    """    Takes a 2d point cloud as input   """
    if not isinstance(points, pd.DataFrame):  ## Vrrifies input is a dataframe. Converts if it isn't
        points = pd.DataFrame(points)
    points.loc()[:, 2] = pow(points.loc()[:, 0], 2) + pow(points.loc()[:,1], 2)  ## Performs parabolic lifting of 2D points to 3D

    plt.scatter(points.loc()[:,0], points.loc()[:,1]) ## Make a plot of the original 2D points

    hull = ConvexHull(points)  ## Performs convex hull on the lifted 3D points

    points = hull.points[:, 0:-1]     ## Puts points in an easier format to work with

    xy_norm = (0, 0, 1) ## Standard normal vector of the XY Plane
        ## Find dot product of this and each simplex, and check that it falls between 0 and -1, exclusive
        ## This would mean the simplex is facing the origonal  coordinate hyperplane and its edges should be inlcuded in the dimensional reduction

    ## Create an array of the dot products of the XY-Plane Normal and al the Facet Normals
    idx = np.shape(hull.equations)[1] - 1
    dot_facets = np.dot(hull.equations[:,0:idx], xy_norm)

    ## Create a list of all the 3D simplices that have dot-product with XY plane between -1 and 0, exclusive
    bool_simplices = hull.simplices[((dot_facets < 0) & (dot_facets > -1)), :]


    ## Reduce list of triangles to only ones that contain the first point.
    ## This step assumes the local optimality of the triangulation given that the neighborhood is large enough
    bool_simplices = [[num for num in row] for row in bool_simplices if 0 in row]
    return bool_simplices
