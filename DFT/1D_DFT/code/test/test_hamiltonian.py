'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-07 14:00:29
LastEditTime : 2022-09-07 17:08:09
FilePath     : /Quantum_Mechanics/DFT/1D_DFT/code/test/test_hamiltonian.py
Description  : 
'''
import unittest
import numpy as np


# python3 -m code.test.test_hamiltonian
from ..driver.hamiltonian import Hamiltonian
from ..driver.solver import Solver
from ..driver.densityCalculator import DensityCalculator


num_grids = 201
xs_lst = np.linspace(-5, 5, num_grids)


class HamiltonianTest(unittest.TestCase):
    def test_operator_kenitic(self):
        hamiltonian = Hamiltonian(xs_lst=xs_lst)

        #print(hamiltonian.operator_kenitic())
        #print(hamiltonian.operator_external())
        #print(hamiltonian.operator_well())
    
    def test_hatree(self):
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic()
        eig_vals_mat_1, eig_psis_mat_1 = \
                        Solver.solve(hamiltonian_matrix)

        density_calculator = DensityCalculator(
                                xs_lst=xs_lst,
                                eig_psis_mat=eig_psis_mat_1,
                                nums_electrons=17)
        density_array_1 = density_calculator.calculate_density()


        print(hamiltonian.operator_hatree(
                        densitys_array=density_array_1, eps=1e-1))
        

    def test_exchange(self):
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic()
        eig_vals_mat_1, eig_psis_mat_1 = \
                        Solver.solve(hamiltonian_matrix)

        density_calculator = DensityCalculator(
                                xs_lst=xs_lst,
                                eig_psis_mat=eig_psis_mat_1,
                                nums_electrons=17)
        density_array_1 = density_calculator.calculate_density()


        print(hamiltonian.operator_exchange(
                        densitys_array=density_array_1))



if __name__ == "__main__":
    unittest.main()