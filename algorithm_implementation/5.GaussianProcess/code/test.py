'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-30 13:42:09
LastEditTime : 2022-10-02 15:21:55
FilePath     : /Quantum_Mechanics/algorithm_implementation/5.GaussianProcess/code/test.py
Description  : 
'''
import numpy as np



def gaussian_kernel(x1:np.array,
                    x2:np.array,
                    l:float=1.0,
                    sigma_f=1.0):
    '''
    Note:
    ----
        1. x1, x2 都需要以列向量形式输入 (x1, x2 都是二维 np.array)
    '''
    dist_matrix = np.sum(np.power(x1, 2), 1).reshape(-1, 1) + \
                np.sum(np.power(x2, 2), 1).reshape(1, -1) - \
                2 * x1 * x2.T
    return np.power(sigma_f, 2) * np.exp(-0.5 * dist_matrix / np.power(l, 2))



if __name__ == "__main__":
    x = np.array([700, 800, 1029]).reshape(-1, 1)
    print(gaussian_kernel(x, x, l=500, sigma_f=10))