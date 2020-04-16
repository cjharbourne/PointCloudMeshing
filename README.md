# PointCloudMeshing

This is for my project in my Geometric Processing course.

It is my current working code, minus all scratch work, temporary files, and intermediate results.
I created dozens of different versions of the script before settling on this variation that gave me the best results.

I have created a script with basic functionalities to create a surface mesh of a 3D point cloud.
It still needs more improvement, as the mesh's are not currently watertight. 
My specific goal was to use parabolic lifting maps to generate a Delaunay Triangulation of a 3D point cloud, 
generating a surface mesh. The first step is to iterate through all the points finding their N nearest neighbors 
via a BallTree. I experimented with a KD-Tree, but had better results with the Ball. After experimenting with 
several metrics for the ball tree, I found that the Euclidean had poor results and I settled on the Bray-Curtis 
dissimilarity measure.
Once I obtained a small neighborhood of points, I performed PCA on them to reduce them to 2D, used the parabolic 
lifting method to triangulate them, and passed these local triangulations back to the main function to merge into 
the list of facets.
I then used several mesh-repairing methods to clean up the surface and reduce the number of imperfections.
