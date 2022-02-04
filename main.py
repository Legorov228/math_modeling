import matplotlib.pyplot as plt
import numpy as np
f = 'ocr and ell'

def grafik(f, rad = 2, a = 2, b = 4, xa = -1, xb = 1, N = 0.001):
  x = np.arange(xa, xb, N)
  y = np.arange(xa, xb, N)
  X, Y = np.meshgrid(x, y)
  if f == 'ocr':
    fxy = x ** 2 + y ** 2
    plt.title('ocr')
    plt.axis('equal')
  elif f == 'ell':
    fxy = x ** 2 / a ** 2 + y ** 2 / b ** 2 - 1
    plt.title('ocr')
    plt.axis('equal')
  plt.control(X, Y, fxy, levels = [0])
  plt.show()
grafik(f = 'ocr')