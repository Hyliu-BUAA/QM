import numpy as np
import matplotlib.pyplot as plt


n = 10      # The number of spaced subintervals
h = (5 - 0) / 10    # The length of subintervals

# 1. Get matrix A
A = np.zeros( (n+1, n+1) )  # 10 subintervals -> 11 points
A[0, 0] = 1
A[n, n] = 1
for i in range(1, n):
    A[i, i-1] = 1
    A[i, i] = -2
    A[i, i+1] = 1
print(A)


# 2. Get b -- row vector
b = np.zeros(n+1)
b[1:-1] = -9.8 * pow(h, 2)
b[-1] = 50
print(b)


# 3. solve the linear equations
y_lst = np.linalg.solve(A, b)


# 4. plot the picture
x_lst = np.linspace(0, 5, 11)

plt.figure(figsize=(10, 8))
plt.plot(x_lst, y_lst, 
        color="steelblue",
        linewidth=3)
plt.scatter(5, 50, s=100, c="red")
## 4.1. Retouch the xlabel, ylabel
plt.xlabel("Times (s)", 
            fontsize=28, 
            fontweight="bold"
)
plt.ylabel("Altitude (m)", 
            fontsize=28, 
            fontweight="bold"
)
# 4.2. Retouch the ticks of x-axis/y-axis
plt.xticks(fontsize=20, 
        fontweight="bold"
        )
plt.yticks(fontsize=20, 
        fontweight="bold"
        )
plt.show()