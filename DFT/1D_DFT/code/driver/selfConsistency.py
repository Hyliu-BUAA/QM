'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-07 17:17:14
LastEditTime : 2022-09-07 19:05:37
FilePath     : /Quantum_Mechanics/DFT/1D_DFT/code/driver/selfConsistency.py
Description  : 
'''
import numpy as np

from ..driver.hamiltonian import Hamiltonian
from ..driver.densityCalculator import DensityCalculator


def print_log(i, log):
    print(f"Step= {i:<5}:  Energy= {log['energy'][-1]:<10.4f}: Energy_DIFF= {log['energy_diff'][-1]:.10f}")


class SelfConsistence(object):
    def __init__(self, 
                xs_lst: np.array,
                num_electrons: int,
                max_iters:int,
                energy_tolerence:float,
                eps:float):
        self.xs_lst = xs_lst
        self.num_electrons = num_electrons
        self.max_iters = max_iters
        self.energy_tolerence = energy_tolerence
        self.eps = eps
        self.log = {"energy":[float("inf")], "energy_diff":[float("inf")]}
        
        self.hamiltonian = Hamiltonian(xs_lst=xs_lst)

    def run(self, densitys_array: np.array):
        for idx in range(self.max_iters):
            # 1. 构造哈密顿量 (根据设定的初始电子密度)
            exchange_energy, exchange_potential_array = \
                                self.hamiltonian.operator_exchange(
                                            densitys_array=densitys_array)
            hatree_energy, hatree_potential_energy = \
                                self.hamiltonian.operator_hatree(
                                            densitys_array=densitys_array,
                                            eps=self.eps)
            hamiltonian_matrix = self.hamiltonian.operator_kenitic() + \
                            self.hamiltonian.operator_external() + \
                            np.diag(exchange_potential_array + hatree_potential_energy, 0)


            # 2. 求解薛定谔方程
            eig_vals_mat, eig_psis_mat = np.linalg.eigh(hamiltonian_matrix)
            self.log["energy"].append(eig_vals_mat[0])
            energy_diff = self.log["energy"][-1] - self.log["energy"][-2]
            self.log["energy_diff"].append(energy_diff)
            print_log(idx, self.log)

            if ( abs(energy_diff) < self.energy_tolerence ):
                break
            
            # 3. 更新态密度
            density_calculator = DensityCalculator(
                                    xs_lst=self.xs_lst,
                                    eig_psis_mat=eig_psis_mat,
                                    nums_electrons=self.num_electrons
                                    )
            densitys_array = density_calculator.calculate_density()