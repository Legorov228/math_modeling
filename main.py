from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import numpy as np

fig = plt.figure()
ax = plt3d.Axes3D(fig)

N = 100
alpha = np.linspace(0, 10, N)

theta = np.linspace(0,10,N)

x = R * np.outer(np.sin(theta), np.cos(alpha))
y = R * np.outer(np.sin(theta), np.sin(alpha))
z = R * np.outer(np.ones(np.size(phi))

ax.plot_surface(x, y, z)
plt.show()