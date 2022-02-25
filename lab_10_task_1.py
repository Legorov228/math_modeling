import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(t, x):
  y, z = t
  dy_dx = y**2*z
  dz_dx = z/x-(y*z)**x
  return dy_dx, dz_dx
y0 = 1
z0 = -3
b = 0.25

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 1], 'b', label='theta(t)')
plt.legend()
plt.show()