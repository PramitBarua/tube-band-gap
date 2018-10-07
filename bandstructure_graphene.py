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
import numpy


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
a0 = 1.42e-10
a = numpy.sqrt(3)*a0
kx = numpy.linspace(-2*numpy.pi, 2*numpy.pi, num=1011)
X, Y = numpy.meshgrid(kx, kx)
E = numpy.sqrt(1+4*numpy.cos(numpy.sqrt(3)*Y/2)*numpy.cos(X/2)+4*numpy.cos(X/2)**2)


ax.plot_surface(X,Y,E,cmap='viridis',vmin=-E.max(),vmax=E.max())#,rstride=1,cstride=1)
ax.plot_surface(X,Y,-E,cmap='viridis',vmin=-E.max(),vmax=E.max())#,rstride=1,cstride=1)

plt.gca().invert_yaxis()

plt.show()
