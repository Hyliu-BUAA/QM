'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-07 14:33:03
LastEditTime : 2022-09-07 20:11:55
FilePath     : /Quantum_Mechanics/DFT/1D_DFT/code/driver/densityCalculator.py
Description  : 
'''
import numpy as np

from .solver import Integrator


class DensityCalculator(object):
    '''
    Description
    ----------- 
        1. 某处 (x) 的态密度等于所有轨道的电子在该处的密度之和
            - n(x) = sum_n{ f_n * |\psi{x}|^2 }
        2. 作用均是密度的泛函：
            - Couloumb interaction
            - Hatree interaction
            - LDA interaction
    
    Note
    ----
        1. 所有波函数需要归一化, 但 `np.linalg.eigh()` 返回的是归一化本征函数
    '''
    def __init__(self,
                xs_lst: np.array,
                eig_psis_mat: np.matrix,
                nums_electrons: int
                ):
        '''
        Parameters
        ----------
            1. eig_psis_mat: np.matrix
                - eigen wavefunction for harmonic oscillator
                - 每一列对应一个本征值的本征波函数
            2. nums_electrons: int
                - numbers of electrons
        '''
        self.xs_lst = xs_lst
        self.eig_psis_mat = eig_psis_mat
        self.num_electrons = nums_electrons

    
    def _get_num_electrons_lst(self):
        '''
        Description
        -----------
            1. 每个轨道可以有两个原子, 且优先占据能量较低的轨道
            2. 被 `self.calcualte_density()` 调用
        
        Return 
        ------
            1. num_electrons_lst: list
                反映了电子占据情况
        '''
        num_electrons_lst = [2 for _ in range(self.num_electrons // 2)]
        if (self.num_electrons % 2):
            num_electrons_lst.append(1)
        
        return num_electrons_lst
    

    def calculate_density(self):
        '''
        Description
        -----------
            1. 某处 (x) 的态密度等于所有轨道的电子在该处的密度之和
            2. Run over all eigen waverfunctions.

        Return
        ------
            1. densitys_array: np.array
                - densitys_arry.shape = (201, )
        '''
        num_electrons_lst = self._get_num_electrons_lst()
        
        # 波函数归一化
        I = Integrator.calculate_integral(xs_array=self.xs_lst, 
                                    ys_array=np.power(self.eig_psis_mat, 2),
                                    axis=0)
        self.eig_psis_mat = self.eig_psis_mat / np.sqrt(I)

        # densitys_array : 列向量
        densitys_mat = np.zeros_like(self.eig_psis_mat[:, 0])
        for num_electrons, psi in zip(num_electrons_lst, self.eig_psis_mat.T):
            densitys_mat += num_electrons * np.power(psi.T, 2)
        
        # After this step, densitys_lst = (201, )
        # Note: 必须先转换为 `np.array` 再使用 `ravel()` 方法
        densitys_array = np.array(densitys_mat).ravel()

        return densitys_array