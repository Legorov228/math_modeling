import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

def diff_func(z, t):
  x, y = z
  dx_dt = 3 * x - 2 * y + e
  dy_dt = 
  return dx_dt, dy_dt
y0 = 5
z0 = -7

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 1], 'b', label='theta(t)')
plt.legend()
plt.show()