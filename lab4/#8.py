from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib.colors import LightSource
from matplotlib import pyplot

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

your_mesh = mesh.Mesh.from_file('Doom combat scene.stl')
axes.add_collection3d(
    mplot3d.art3d.Poly3DCollection(
         your_mesh.vectors,
         cmap='hot'
    ))
scale = your_mesh.points.flatten("K")
axes.auto_scale_xyz(scale, scale, scale)

ls = LightSource(azdeg=225.0, altdeg=45.0)

pyplot.show()