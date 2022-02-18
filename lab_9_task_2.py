import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 4, 0.01)

def inv(i, t):
  didt = - k * i * t
  return didt

i_0 = 1000
k = 0.08

solve_Bi = odeint(inv, i_0, t)

plt.plot(t, solve_Bi[:,0], label='Уменьшение инвестиций')
plt.xlabel('Период уменьшение, лет')
plt.ylabel('Функция уменьшение')
plt.title('Real life')
plt.legend()

plt.show()