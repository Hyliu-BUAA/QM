'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-07 13:31:23
LastEditTime : 2022-09-07 17:14:49
FilePath     : /Quantum_Mechanics/DFT/1D_DFT/code/driver/hamiltonian.py
Description  : 
'''
import numpy as np

from .solver import Integrator


class Hamiltonian(object):
    '''
    Attributes
    ----------
        1. self.xs_lst: list
            The coordination of harmonic oscillator
        2. self.dx: float
            The interval of xs_lst
        3. self.num_grids: int
            The number of grids' points
    '''
    def __init__(self,
                xs_lst:list,
                ):
        '''
        Parameters
        ----------
            1. xs_lst: list
                The coordination of harmonic oscillator
        '''
        self.xs_lst = xs_lst
        self.dx = np.diff(xs_lst).mean()
        self.num_grids = len(self.xs_lst)
    

    def operator_kenitic(self):
        '''
        Description
        -----------
            1. df(x)/dx2 = ( f(x+dx) - 2f(x) + f(x-dx) ) / dx2
            2. operator_kenitic = - 1/2 df(x)/dx2
        '''
        dia = -2 * np.ones(self.num_grids)
        offdia = np.ones(self.num_grids - 1)
        derivative_x2 = np.mat(
                np.diag(dia, 0) + np.diag(offdia, 1) + np.diag(offdia, -1)
                )
        derivative_x2 = derivative_x2 / np.power(self.dx, 2)
        operator_kenitic = - 1 / 2 * derivative_x2
        
        return operator_kenitic


    def operator_external(self):
        '''
        Description
        -----------
            1. operator_external = x^2
        '''
        operator_external = np.power(self.xs_lst, 2)
        operator_external = np.diag(operator_external, 0)
    
        return operator_external
    

    def operator_well(self):
        '''
        Description
        -----------
            1. 1D well potential
        '''
        operator_well = np.full_like(self.xs_lst, 1e10)
        operator_well[np.logical_and(self.xs_lst>-2, self.xs_lst<2)] = 0
        operator_well = np.diag(operator_well, 0)
        
        return operator_well


    def operator_exchange(self, densitys_array: np.array):
        '''
        Description
        ----------- 
            1. Consider the exchange functional in the LDA
                (Local Density Approximation)
        
        Parameters
        ----------
            1. densitys_lst: np.array
                - 1D np.array, densitys_array.shape(201,)

        Return 
        ------
            1. exchange_energy: float

            2. exchange_potentials_array: np.array
                potentials_array.shape = (201,)
        '''
        exchange_energy = -3/4 * np.power(3/np.pi, 1/3) * \
                Integrator.calculate_integral(xs_array=self.xs_lst,
                                            ys_array=densitys_array,
                                            axis=0)
        exchange_potentials_array = -np.power(3/np.pi, 1/3) * \
                            np.power(densitys_array, 1/3)

        return exchange_energy, exchange_potentials_array

    

    def operator_hatree(self, densitys_array: np.array, eps:float):
        '''
        Description
        -----------
            1. Coulomb energy (also called Hatree energy)
            2. The expression if 3D-hatree energy is not convergence in 1D
        
        Parameters
        ----------
            1. densitys_lst: np.array
                - 1D np.array, densitys_array.shape(201,)

        Return 
        ------
            1. hatree_energy: float

            2. hartree_potentials_array: np.array
                potentials_array.shape = (201,)

        Note
        ----
            python> lst = np.array([1,2,3])
            python> lst_1 = lst[None, :]
            python> lst_2 = lst[:, None]

            python> lst
            [[1 2 3]]

            python> lst_2
            [[1]
            [2]
            [3]]

            python> lst_1 * lst_2
            [[1 2 3]
            [2 4 6]
            [3 6 9]]
        '''
        dx = np.diff(self.xs_lst).mean()
        
        # 2D-array -> float
        hartree_energy = np.sum( densitys_array[None, :] * densitys_array[:, None] * \
                            np.power(dx, 2) / \
                            np.sqrt(np.power(self.xs_lst[None, :] - self.xs_lst[:, None], 2) + eps)
                            ) / 2
        hartree_potentials_lst = np.sum( densitys_array[None, :] * dx / \
                                np.sqrt( np.power(self.xs_lst[None, :] - self.xs_lst[:, None], 2) + eps ),
                                axis=1
                                )
        
        return hartree_energy, hartree_potentials_lst