import matplotlib.pyplot as plt
import numpy as np
f = 'par and gep'

def grafik(f,a = 2, b = 4, c = 3, k = 2, xa = -100, xb = 100, N = 0.0001):
  x = np.arange(xa, xb, N)
  if f == 'par':
    y = a * x ** 2 + b * x + c
    plt.title('Парабола')
  elif f == 'gep':
    y = k / x
    plt.title('Гипербола')
  plt.plot(x, y)
  plt.show()
grafik(f = 'par')