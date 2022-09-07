'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-07 14:10:04
LastEditTime : 2022-09-07 16:31:41
FilePath     : /Quantum_Mechanics/DFT/1D_DFT/code/driver/solver.py
Description  : 
'''
import numpy as np


class Solver(object):
    @staticmethod
    def solve(hamiltonian_matrix:np.matrix):
        '''
        Return
        ------
            1. eig_vals_mat: np.matrix
                - eig_vals_mat.shape = (201,)
            2. eig_psis_mat: np.matrix
                - eig_vals_mat.shape = (201, 201)
                - 每一列对应一个本征值的本征波函数

        Note
        ----
            1. The column `eig_psis_mat[:, i]` is the 
                `normalized eigenvector`
                corresponding to the eigenvalue `eig_vals_mat[i]`.
        '''
        eig_vals_mat, eig_psis_mat = np.linalg.eigh(hamiltonian_matrix)
        return eig_vals_mat, eig_psis_mat



class Integrator(object):
    @staticmethod
    def calculate_integral(xs_array: np.array, ys_array: np.array, axis: int):
        '''
        Note
        ----    
            1. $ arr1 = np.array([1, 2, 3])
               $ np.sum(arr1, axis=0)
               6
        '''
        dx = np.diff(xs_array).mean()
        return np.sum(ys_array * dx, axis=axis)