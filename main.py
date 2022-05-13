import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years * seconds_in_year, frames)

def move_func(s, t):
  (x1, v_x1, y1, v_y1,
   x2, v_x2, y2, v_y2,
   x3, v_x3, y3, v_y3,
   x4, v_x4, y4, v_y4,
   x5, v_x5, y5, v_y5,
   x6, v_x6, y6, v_y6) = s

  dxdt1 = v_x1
  dv_xdt1 = - G * m * x1 / (x1**2 + y1**2)**1.5
  dydt1 = v_y1
  dv_ydt1 = - G * m * y1 / (x1**2 + y1**2)**1.5
  
  dxdt2 = v_x2
  dv_xdt2 = - G * m * x2 / (x2**2 + y2**2)**1.5
  dydt2 = v_y2
  dv_ydt2 = - G * m * y2 / (x2**2 + y2**2)**1.5

  dxdt3 = v_x3
  dv_xdt3 = - G * m * x3 / (x3**2 + y3**2)**1.5
  dydt3 = v_y3
  dv_ydt3 = - G * m * y3 / (x3**2 + y3**2)**1.5

  dxdt4 = v_x4
  dv_xdt4 = - G * m * x4 / (x4**2 + y4**2)**1.5
  dydt4 = v_y4
  dv_ydt4 = - G * m * y4 / (x4**2 + y4**2)**1.5

  dxdt5 = v_x5
  dv_xdt5 = - G * m * x5 / (x5**2 + y5**2)**1.5
  dydt5 = v_y5
  dv_ydt5 = - G * m * y5 / (x5**2 + y5**2)**1.5

  dxdt6 = v_x6
  dv_xdt6 = - G * m * x6 / (x6**2 + y6**2)**1.5
  dydt6 = v_y6
  dv_ydt6 = - G * m * y6 / (x6**2 + y6**2)**1.5

  return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
          dxdt2, dv_xdt2, dydt2, dv_ydt2,
          dxdt3, dv_xdt3, dydt3, dv_ydt3,
          dxdt4, dv_xdt4, dydt4, dv_ydt4,
          dxdt5, dv_xdt5, dydt5, dv_ydt5,
          dxdt6, dv_xdt6, dydt6, dv_ydt6)

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x10 = 57.91 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 47360

x20 = 108 * 10**9
v_x20 = 0
y20 = 0
v_y20 = 35020

x30 = 149.6 * 10**9
v_x30 = 0
y30 = 0
v_y30 = 29783

x40 = 206.6 * 10**9
v_x40 = 0
y40 = 0
v_y40 = 24130

x50 = 152.14 * 10**9
v_x50 = 0
y50 = 0
v_y50 = 20122

x60 = 400 * 10**9
v_x60 = -34000
y60 = 0
v_y60 = 15000

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60)

sol = odeint(move_func, s0, t)
def solve_func(i, key):
  if key == 'point':
    x1 = sol[i, 0]
    y1 = sol[i, 2]
    x2 = sol[i, 4]
    y2 = sol[i, 6]
    x3 = sol[i, 8]
    y3 = sol[i, 10]
    x4 = sol[i, 12]
    y4 = sol[i, 14]
    x5 = sol[i, 16]
    y5 = sol[i, 18]
    x6 = sol[i, 20]
    y6 = sol[i, 22]
  else:
    x1 = sol[i, 0]
    y1 = sol[i, 2]
    x2 = sol[i, 4]
    y2 = sol[i, 6]
    x3 = sol[i, 8]
    y3 = sol[i, 10]
    x4 = sol[i, 12]
    y4 = sol[i, 14]
    x5 = sol[i, 16]
    y5 = sol[i, 18]
    x6 = sol[i, 20]
    y6 = sol[i, 22]
  return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6))

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='peru')
ball_line1, = plt.plot([], [], '-', color='peru')

ball2, = plt.plot([], [], 'o', color='sienna')
ball_line2, = plt.plot([], [], '-', color='sienna')

ball3, = plt.plot([], [], 'o', color='b')
ball_line3, = plt.plot([], [], '-', color='b')

ball4, = plt.plot([], [], 'o', color='r')
ball_line4, = plt.plot([], [], '-', color='r')

ball5, = plt.plot([], [], 'o', color='silver')
ball_line5, = plt.plot([], [], '-', color='silver')

ball6, = plt.plot([], [], 'o', color='gold', ms=20)
ball_line6, = plt.plot([], [], '-', color='gold')

plt.plot([0], [0], 'o', color='y', ms=15)

def animate(i):
  ball1.set_data(solve_func(i, 'point')[0])
  ball_line1.set_data(solve_func(i, 'line')[0])

  ball2.set_data(solve_func(i, 'point')[1])
  ball_line2.set_data(solve_func(i, 'line')[1])

  ball3.set_data(solve_func(i, 'point')[2])
  ball_line3.set_data(solve_func(i, 'line')[2])

  ball4.set_data(solve_func(i, 'point')[3])
  ball_line4.set_data(solve_func(i, 'line')[3])

  ball5.set_data(solve_func(i, 'point')[4])
  ball_line5.set_data(solve_func(i, 'line')[4])
  
  ball6.set_data(solve_func(i, 'point')[5])
  ball_line6.set_data(solve_func(i, 'line')[5])

ani = FuncAnimation(fig,
                   animate,
                   frames=frames,
                   interval=30)

plt.axis('equal')
edge = 10 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()