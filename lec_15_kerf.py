import numpy as np
import matplotlib.pyplot as plt
import mpl_toollkits.mplot3d.axes3d as plt3d

fig = plt.figure()
ax = plt3d.Axes3D(fig)

t = np.arange(0.01, 4 * np.pi, 0.01)
R = 1

x = R * np.cos(t)
y = R * t ** 0.5
z = np.log10(t)

ax.plot(x, y, z, label='Dich')
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Test')
plt.show()