import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as plt3d

fig = plt.figure()
ax = plt3d.Axes3D(fig)

# Определение параметров пространственной кривой
N = 100
alpha = np.linspace(0, 10, N)

# Параметрическое задание пространственной кривой
x = np.cos(alpha)
y = np.sin(alpha)
z = alpha * 0

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years * seconds_in_year, frames)

def move_func(s, t):
  (x1, v_x1, y1, v_y1, z1, v_z1,
   x2, v_x2, y2, v_y2, z2, v_z2,
   x3, v_x3, y3, v_y3, z3, v_z3,
   x4, v_x4, y4, v_y4, z4, v_z4,
   x5, v_x5, y5, v_y5, z5, v_z5) = s

  dxdt1 = v_x1
  dv_xdt1 = - G * m * x1 / (x1**2 + y1**2 + z1**2)**1.5
  dydt1 = v_y1
  dv_ydt1 = - G * m * y1 / (x1**2 + y1**2 + z1**2)**1.5
  dzdt1 = v_z1
  dv_zdt1 = - G * m * z1 / (x1**2 + y1**2 + z1**2)**1.5
  
  dxdt2 = v_x2
  dv_xdt2 = - G * m * x2 / (x2**2 + y2**2 + z2**2)**1.5
  dydt2 = v_y2
  dv_ydt2 = - G * m * y2 / (x2**2 + y2**2 + z2**2)**1.5
  dzdt2 = v_z2
  dv_zdt2 = - G * m * z2 / (x2**2 + y2**2 + z2**2)**1.5

  dxdt3 = v_x3
  dv_xdt3 = - G * m * x3 / (x3**2 + y3**2 + z3**2)**1.5
  dydt3 = v_y3
  dv_ydt3 = - G * m * y3 / (x3**2 + y3**2 + z3**2)**1.5
  dzdt3 = v_z3
  dv_zdt3 = - G * m * z3 / (x3**2 + y3**2 + z3**2)**1.5

  dxdt4 = v_x4
  dv_xdt4 = - G * m * x4 / (x4**2 + y4**2 + z4**2)**1.5
  dydt4 = v_y4
  dv_ydt4 = - G * m * y4 / (x4**2 + y4**2 + z4**2)**1.5
  dzdt4 = v_z4
  dv_zdt4 = - G * m * z4 / (x4**2 + y4**2 + z4**2)**1.5

  dxdt5 = v_x5
  dv_xdt5 = - G * m * x5 / (x5**2 + y5**2 + z5**2)**1.5
  dydt5 = v_y5
  dv_ydt5 = - G * m * y5 / (x5**2 + y5**2 + z5**2)**1.5
  dzdt5 = v_z5
  dv_zdt5 = - G * m * z5 / (x5**2 + y5**2 + z5**2)**1.5

  return (dxdt1, dv_xdt1, dydt1, dv_ydt1, dzdt1, dv_zdt1,
          dxdt2, dv_xdt2, dydt2, dv_ydt2, dzdt2, dv_zdt2,
          dxdt3, dv_xdt3, dydt3, dv_ydt3, dzdt3, dv_zdt3,
          dxdt4, dv_xdt4, dydt4, dv_ydt4, dzdt4, dv_zdt4,
          dxdt5, dv_xdt5, dydt5, dv_ydt5, dzdt5, dv_zdt5)

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x10 = 57.91 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 47360
z10 = 0
v_z10 = 0

x20 = 149.6 * 10**9
v_x20 = 0
y20 = 0
v_y20 = 35020
z20 = 0
v_z20 = 0

x30 = 108 * 10**9
v_x30 = 0
y30 = 0
v_y30 = 29783
z30 = 0
v_z30 = 0

x40 = 228 * 10**9
v_x40 = 0
y40 = 0
v_y40 = 24130
z40 = 0
v_z40 = 0

x50 = 189 * 10**9
v_x50 = 0
y50 = 0
v_y50 = 20122
z50 = 0
v_z50 = 0

s0 = (x10, v_x10, y10, v_y10, z10, v_z10,
      x20, v_x20, y20, v_y20, z20, v_z20,
      x30, v_x30, y30, v_y30, z30, v_z30,
      x40, v_x40, y40, v_y40, z40, v_z40,
      x50, v_x50, y50, v_y50, z50, v_z50)

sol = odeint(move_func, s0, t)
def solve_func(i, key):
  if key == 'point':
    x1 = sol[i, 0]
    y1 = sol[i, 2]
    z1 = sol[i, 4]
    x2 = sol[i, 6]
    y2 = sol[i, 8]
    z2 = sol[i, 10]
    x3 = sol[i, 12]
    y3 = sol[i, 14]
    z3 = sol[i, 16]
    x4 = sol[i, 18]
    y4 = sol[i, 20]
    z4 = sol[i, 22]
    x5 = sol[i, 24]
    y5 = sol[i, 26]
    z5 = sol[i, 28]
  else:
    x1 = sol[i, 0]
    y1 = sol[i, 2]
    z1 = sol[i, 4]
    x2 = sol[i, 6]
    y2 = sol[i, 8]
    z2 = sol[i, 10]
    x3 = sol[i, 12]
    y3 = sol[i, 14]
    z3 = sol[i, 16]
    x4 = sol[i, 18]
    y4 = sol[i, 20]
    z4 = sol[i, 22]
    x5 = sol[i, 24]
    y5 = sol[i, 26]
    z5 = sol[i, 28]
  return ((x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4), (x5, y5, z5))

fig, ax = plt.subplots()

ball1, = ax.plot(solve_func(0, 'point')[0], 'o', color='peru')
line1, = ax.plot(solve_func(0, 'line')[0], '-', color='peru')

ball2, = ax.plot(solve_func(0, 'point')[1], 'o', color='sienna')
line2, = ax.plot(solve_func(0, 'line')[1], '-', color='sienna')

ball3, = ax.plot(solve_func(0, 'point')[2], 'o', color='b')
line3, = ax.plot(solve_func(0, 'line')[2], '-', color='b')

ball4, = ax.plot(solve_func(0, 'point')[3], 'o', color='r')
line4, = ax.plot(solve_func(0, 'line')[3], '-', color='r')

ball5, = ax.plot(solve_func(0, 'point')[4], 'o', color='silver')
line5, = ax.plot(solve_func(0, 'line')[4], '-', color='silver')

plt.plot([0], [0], 'o', color='y', ms=15)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0][0], solve_func(i, 'point')[0][1])
    ball1.set_3d_properties(solve_func(i, 'point')[0][2])

    line1.set_data(solve_func(i, 'line')[0][0], solve_func(i, 'line')[0][1])
    line1.set_3d_properties(solve_func(i, 'line')[0][2])

    ball2.set_data(solve_func(i, 'point')[1][0], solve_func(i, 'point')[1][1])
    ball2.set_3d_properties(solve_func(i, 'point')[1][2])

    line2.set_data(solve_func(i, 'line')[1][0], solve_func(i, 'line')[1][1])
    line2.set_3d_properties(solve_func(i, 'line')[1][2])

    ball3.set_data(solve_func(i, 'point')[2][0], solve_func(i, 'point')[2][1])
    ball3.set_3d_properties(solve_func(i, 'point')[2][2])

    line3.set_data(solve_func(i, 'line')[2][0], solve_func(i, 'line')[2][1])
    line3.set_3d_properties(solve_func(i, 'line')[2][2])

    ball4.set_data(solve_func(i, 'point')[3][0], solve_func(i, 'point')[3][1])
    ball4.set_3d_properties(solve_func(i, 'point')[3][2])

    line4.set_data(solve_func(i, 'line')[3][0], solve_func(i, 'line')[3][1])
    line4.set_3d_properties(solve_func(i, 'line')[3][2])

    ball5.set_data(solve_func(i, 'point')[4][0], solve_func(i, 'point')[4][1])
    ball5.set_3d_properties(solve_func(i, 'point')[4][2])

    line5.set_data(solve_func(i, 'line')[4][0], solve_func(i, 'line')[4][1])
    line5.set_3d_properties(solve_func(i, 'line')[4][2])

ani = FuncAnimation(fig, animate, N, interval=50)

plt.show()