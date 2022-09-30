'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-30 11:45:47
LastEditTime : 2022-09-30 11:54:04
FilePath     : /Quantum_Mechanics/algorithm_implementation/5.GaussianProcess/code/gaussian_kernel.py
Description  : 
'''
import numpy as np


def gaussian_kernel(array1: np.array,
                    array2:np.array,
                    l:float,
                    sigma:float):
    "Easy to understand but inefficient"
    dim1, dim2 = array1.shape[0], array2.shape[0]
    dist_matrix = np.zeros((dim1, dim2), dtype=float)

    for i in range(dim1):
        for j in range(dim2):
            dist_matrix[i][j] = np.sum(array1[i] - array2[j])
    
    return np.power(sigma, 2) * np.exp(-0.5 * np.power(dist_matrix, 2) / np.power(l, 2))


if __name__ == "__main__":
    x = np.array([700, 800, 1029]).reshape(-1, 1)
    print( gaussian_kernel(x, x, l=500, sigma=10))