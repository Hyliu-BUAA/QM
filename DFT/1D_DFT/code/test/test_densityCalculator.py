'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-07 15:33:53
LastEditTime : 2022-09-07 18:04:12
FilePath     : /Quantum_Mechanics/DFT/1D_DFT/code/test/test_densityCalculator.py
Description  : 
'''
import unittest
import numpy as np
import matplotlib.pyplot as plt

# python3 -m code.test.test_densityCalculator
from ..driver.hamiltonian import Hamiltonian
from ..driver.solver import Solver
from ..driver.densityCalculator import DensityCalculator


num_grids = 201
xs_lst = np.linspace(-5, 5, num_grids)

dc_jpg_path = "/Users/mac/我的文件/Notebook/Quantum_Mechanics/DFT/1D_DFT/code/output/density_coordination.jpg"
dval_jpg_path = "/Users/mac/我的文件/Notebook/Quantum_Mechanics/DFT/1D_DFT/code/output/density_eigenval.jpg"


class DensityCalculatorTest(unittest.TestCase):
    def test_calculate_density(self):
        ### Part I. Solve the equation
        # 1. None
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic()
        eig_vals_mat_1, eig_psis_mat_1 = \
                        Solver.solve(hamiltonian_matrix)
        
        # 2. external
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic() +\
                            hamiltonian.operator_external()
        eig_vals_mat_2, eig_psis_mat_2 = \
                        Solver.solve(hamiltonian_matrix)

        # 3. well
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic() +\
                            hamiltonian.operator_well()
        eig_vals_mat_3, eig_psis_mat_3 = \
                        Solver.solve(hamiltonian_matrix)       
        

        ### Part II. Get the density
        # 1. None
        density_calculator = DensityCalculator(
                                xs_lst=xs_lst,
                                eig_psis_mat=eig_psis_mat_1,
                                nums_electrons=17)
        density_array_1 = density_calculator.calculate_density()
        
        # 2. external
        density_calculator = DensityCalculator(
                                xs_lst=xs_lst,
                                eig_psis_mat=eig_psis_mat_2,
                                nums_electrons=17)
        density_array_2 = density_calculator.calculate_density()

        # 3. well
        density_calculator = DensityCalculator(
                                xs_lst=xs_lst,
                                eig_psis_mat=eig_psis_mat_3,
                                nums_electrons=17)
        density_array_3 = density_calculator.calculate_density()


        ### Part III.
        # 1. 
        plt.figure(figsize=(10, 8))
        plt.plot(xs_lst, density_array_1, label="none")
        plt.plot(xs_lst, density_array_2, label="external")
        plt.plot(xs_lst, density_array_3, label="well")
        plt.xlabel("X coordination", fontsize=20)
        plt.ylabel("Density", fontsize=20)
        plt.legend()

        plt.savefig(dc_jpg_path, dpi=300, bbox_inches="tight")


        # 2. 
        plt.figure(figsize=(10, 8))
        print(eig_psis_mat_1)
        plt.scatter(eig_vals_mat_1, density_array_1, label="none")
        plt.scatter(eig_vals_mat_2, density_array_2, label="external")
        plt.scatter(eig_vals_mat_3, density_array_3, label="well")
        plt.xlabel("Eigenval", fontsize=20)
        plt.ylabel("Density", fontsize=20)
        plt.legend()

        plt.savefig(dval_jpg_path, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    unittest.main()