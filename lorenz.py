#--Code to integrate the Lorenz system in time,
#--and plot a nice "butterfly" curve

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

#--Coefficients
sigma = 10.
rho = 28.
beta = 8/3.

#--Time derivatives
def f(X, t):
  x, y, z = X
  dxdt = sigma*(y-x)
  dydt = x*(rho-z) - y
  dzdt = x*y - beta*z
  return dxdt, dydt, dzdt

#--Integration time and timestep
tf=50.
dt=0.01
t = np.arange(0.0,tf,dt)

#--Initial conditions
X0 = [1., 1., 1.]

#--Integration
sol = odeint(f, X0, t)
x=sol[:,0]
y=sol[:,1]
z=sol[:,2]

#--Get start and end point of the integration
x0,y0,z0=x[0],y[0],z[0]
xf,yf,zf=x[-1],y[-1],z[-1]

#--Plot
fig = plt.figure(num="Lorenz attractor")
ax = plt.axes(projection='3d')
ax.plot(x,y,z,"C1-", lw=0.5)
#--Add start and end point of the integration
ax.plot([x0],[y0],[z0],marker='o',markerfacecolor='C1', markeredgecolor='w')
ax.plot([xf],[yf],[zf],marker='P',markerfacecolor='C1', markeredgecolor='w')
#--Add a black background
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.grid(False)
ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
#
plt.tight_layout()
plt.show()
