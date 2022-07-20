import numpy as np
from scipy.signal import square
import matplotlib.pyplot as plt
from scipy.integrate import simps


start_point = 0
end_point = 4
L = end_point - start_point
number_points = 1000

frequency = 5
number_terms = 100


# 1. Generation of square
ts_lst = np.linspace(start_point,
                    end_point,
                    number_points,
                    endpoint=False)
signals_lst = square(2 * np.pi * frequency / L * ts_lst) 


# 2. Calculation of Fourier coefficients
A_0 = 2 / L * simps(y=signals_lst, x=ts_lst)
A_k_func = lambda k: 2 / L * simps(signals_lst * np.cos(2*np.pi*k*ts_lst/L), ts_lst)
B_k_func = lambda k: 2 / L * simps(signals_lst * np.sin(2*np.pi*k*ts_lst/L), ts_lst)


# 3. sum of the series
s= A_0/2.+  \
    sum([A_k_func(k)*np.cos(2.*np.pi*k*ts_lst/L) + \
        B_k_func(k)*np.sin(2.*np.pi*k*ts_lst/L)
        for k in range(1, number_terms+1)])


plt.plot(ts_lst, s)
plt.plot(ts_lst, signals_lst)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()