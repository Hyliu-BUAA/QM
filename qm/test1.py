import numpy as np
from scipy.signal import square
from scipy.integrate import simps
import matplotlib.pyplot as plt

number_terms = 500
L = 2

# Sample at 1000 Hz / second
ts_lst = np.linspace(0, L, 5000, endpoint=False)

# The frequency of wave is 5 Hz
signals_lst = square(2 * np.pi * 5 * ts_lst)


# Calculate Fourier coefficient
a_0 = 2 / L * simps(signals_lst, ts_lst)
a_k = lambda k: 2 / L * simps( 
            np.cos(k*2*np.pi*ts_lst*5/L)*signals_lst, 
            ts_lst)
b_k = lambda k: 2 / L * simps(
            np.sin(k*2*np.pi*ts_lst*5/L)*signals_lst,
            ts_lst )

s= a_0/2 +  \
    sum([a_k(k)*np.cos(2.*np.pi*k*ts_lst*5/L) + \
        b_k(k)*np.sin(2.*np.pi*k*ts_lst*5/L)
        for k in range(1, number_terms+1)])

plt.plot(ts_lst, signals_lst)
plt.plot(ts_lst, s)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()