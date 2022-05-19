import numpy as np
from scipy.integrate import odeint

init = -2, 2
def f(y, x):
    y0 = y[0]
    y1 = y[1]
    y2 = 4*y1 - 3*y0
    return y1, y2
X_1 = np.linspace(-100, 1, 100)    
solution = odeint(f, init, X_1)
print('Решение 1:', solution)

init = -2, 2
def f(y, x):
    y0 = y[0]
    y1 = y[1]
    y2 = 4*y1 - 3*y0 + np.sin(x)
    return y1, y2
X_1 = np.linspace(-100, 1, 100)    
solution = odeint(f, init, X_1)
print('Решение 2:', solution)

init = 2.7, 3.5
def system(u, t):
    x=u[0]  
    y=u[1]   
    dx_dt = x - y
    dy_dt = -4*x + 4*x
    return [dx_dt, dy_dt]
t = np.linspace(-100, 1, 100)
solution = odeint(system, init, t)
print('Решение 3:', solution)