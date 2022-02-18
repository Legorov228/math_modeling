import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.001)

def raz_bak(m, t):
  a = k * m
  return a

m_0 = 1
k = 2

solve_Bi = odeint(raz_bak, m_0, t)

plt.plot(t, solve_Bi[:,0], label='Размножение бактерий')
plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Real life')
plt.legend()

plt.show()