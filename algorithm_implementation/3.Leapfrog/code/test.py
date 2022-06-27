import numpy as np
import matplotlib.pyplot as plt

# Solve x" = f(x) using leapfrog integrator

# For this demo, x'' + x = 0
# Exact solution is x(t) = sin(t)
def f(x):
    return -x

num_cycles = 5                          # number of periods
num_points_per_cyle = 16                # number of time steps per period
h = 2*np.pi / num_points_per_cyle       # step size

x = np.empty( num_cycles * num_points_per_cyle + 1 )    # positions
v = np.empty( num_cycles * num_points_per_cyle + 1 )    # velocities

# Initial conditions
# Note: you should set the origin x and origin v carefully (according to `sin(x)` here)
x[0] = 0
a = f(x[0])
v[0] = 1

# leapfrog method
for i in range(1, num_cycles * num_points_per_cyle + 1):
    x[i] = x[i-1] + v[i-1] * h     
    a = f(x[i])
    v[i] = v[i-1] + a * h

t = np.linspace(0, 2*np.pi*num_cycles, num_cycles * num_points_per_cyle + 1)
plt.plot(t, x)
plt.show()