from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import numpy as np

fig = plt.figure()
ax = plt3d.Axes3D(fig)

N = 100
alpha = np.linspace(0, 10, N)

φ = np.linspace(0,10,N)

x = np.outer(φ, np.cos(alpha))
y = np.outer(φ, np.sin(alpha))
z = np.outer(np.ones(np.size(φ)), alpha ** 2)

ax.plot_surface(x, y, z)
plt.show()