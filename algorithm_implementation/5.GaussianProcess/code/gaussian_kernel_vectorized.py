'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-30 11:45:47
LastEditTime : 2022-09-30 12:00:56
FilePath     : /Quantum_Mechanics/algorithm_implementation/5.GaussianProcess/code/test.py
Description  : 
'''
import numpy as np


def gaussian_kernel(x1:np.array, x2:np.array, l:float=1.0, sigma:float=1.0):
    "More efficient approach"
    dist_matrix = np.sum(x1**2, 1).reshape(-1, 1) + np.sum(x2**2, 1) - 2 * np.matmul(x1, x2.T)
    return sigma ** 2 * np.exp(-0.5 / l ** 2 * dist_matrix)


x = np.array([700, 800, 1029]).reshape(-1, 1)
print(gaussian_kernel(x, x, l=500, sigma=10))