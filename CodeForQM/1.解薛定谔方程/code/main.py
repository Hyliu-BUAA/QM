import numpy as np
import matplotlib.pyplot as plt


# 1. Get matrix A and b
def get_A_b(num_intervals:int):
    h = (np.pi/2 - 0) / num_intervals     # The length of subintervals
    x_lst = np.linspace(0, np.pi/2, num_intervals+1)
    
    ## 1.1. Get A
    A = np.zeros((num_intervals+1, num_intervals+1))
    A[0, 0] = 1
    A[num_intervals, num_intervals-1] = 2
    A[num_intervals, num_intervals] = 4 * pow(h, 2) - 2
    for i in range(1, num_intervals):
        A[i, i-1] = 1
        A[i, i] = 4 * pow(h, 2) - 2 
        A[i, i+1] = 1
    
    ## 1.2. Get b
    b = np.zeros(num_intervals + 1)
    for i in range(1, num_intervals+1):
        b[i] = 4 * pow(h, 2) * x_lst[i]
    
    return A, b


# 2. value calculated by Analytic solution
x_target = np.pi / 2    # 计算解析解 f(x) 在 x_target 处的值
func_value_analytic = x_target - np.sin(2*x_target)


# 3. 
ns_lst = []
errors_lst = []
for n_value in range(3, 100, 5):
    A, b = get_A_b(n_value)
    y = np.linalg.solve(A, b)
    
    ns_lst.append(n_value)
    errors_lst.append(func_value_analytic - y[-1])




# 4. plot the picture
x_lst = np.linspace(0, 5, 11)

plt.figure(figsize=(10, 8))
plt.plot(ns_lst, errors_lst, 
        color="steelblue",
        linewidth=3)
plt.yscale('log')   # 纵坐标变成指数坐标

## 4.1. Retouch the xlabel, ylabel
plt.xlabel("Number of intervals", 
            fontsize=28, 
            fontweight="bold"
)
plt.ylabel("Errors at x=$\pi/2$", 
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