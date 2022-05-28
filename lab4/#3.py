from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T 
z = x/y - y/x

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')

ax.plot_surface(x, y, z)
plt.show()