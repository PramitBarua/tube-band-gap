#!/usr/bin/env python3

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2018, INT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "INT, KIT"
__version__ = "1"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]

# band structure of graphene

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy
# import math

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
a0 = 1.42e-10
a = numpy.sqrt(3)*a0
kx = numpy.linspace(-2*numpy.pi, 2*numpy.pi, num=1011)
X, Y = numpy.meshgrid(kx, kx)
E = numpy.sqrt(1+4*numpy.cos(numpy.sqrt(3)*Y/2)*numpy.cos(X/2)+4*numpy.cos(X/2)**2)
# E = numpy.sqrt(1+4*numpy.cos(3*Y)*numpy.cos(numpy.sqrt(3)*X)+4*numpy.cos(numpy.sqrt(3)*X)**2)

# R = numpy.sqrt(X**2 + Y**2)
# Z = numpy.sin(R)

# Plot the surface.
# surf1 = ax.plot_surface(X/numpy.pi, Y/numpy.pi, E, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# surf2 = ax.plot_surface(X/numpy.pi, Y/numpy.pi, -E, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.plot_surface(X,Y,E,cmap='viridis',vmin=-E.max(),vmax=E.max())#,rstride=1,cstride=1)
ax.plot_surface(X,Y,-E,cmap='viridis',vmin=-E.max(),vmax=E.max())#,rstride=1,cstride=1)

# max_range = numpy.array([X.max()-X.min(), Y.max()-Y.min()]).max() / 2.0
# 
# mid_x = (X.max()+X.min()) * 0.5
# mid_y = (Y.max()+Y.min()) * 0.5
# ax.set_xlim(mid_x - max_range, mid_x + max_range)
# ax.set_ylim(mid_y - max_range, mid_y + max_range)
plt.gca().invert_yaxis()
# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
# fig.colorbar(surf1, shrink=0.5, aspect=5)
# fig.colorbar(surf2, shrink=0.5, aspect=5)

plt.show()