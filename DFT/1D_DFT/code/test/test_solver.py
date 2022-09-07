import unittest
import numpy as np
import matplotlib.pyplot as plt

# python3 -m code.test.test_solver
from ..driver.hamiltonian import Hamiltonian
from ..driver.solver import Solver


num_grids = 201
xs_lst = np.linspace(-5, 5, num_grids)

psi5_jpg_1_path = "/Users/mac/我的文件/Notebook/Quantum_Mechanics/DFT/1D_DFT/code/output/psi5_1.jpg"
psi5_jpg_2_path = "/Users/mac/我的文件/Notebook/Quantum_Mechanics/DFT/1D_DFT/code/output/psi5_2.jpg"
psi5_jpg_3_path = "/Users/mac/我的文件/Notebook/Quantum_Mechanics/DFT/1D_DFT/code/output/psi5_3.jpg"


class SolverTest(unittest.TestCase):
    def test_solve_1(self):
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic()

        eig_vals_mat, eig_psis_mat = \
                        Solver.solve(hamiltonian_matrix)
        print(eig_vals_mat.shape)
        print(eig_psis_mat.shape)

        # 绘图
        plt.figure(figsize=(10, 8))
        for idx in range(5):
            plt.plot(xs_lst, eig_psis_mat[:, idx])
        plt.xlabel("1D coordination", fontsize=20)
        plt.ylabel("Psi", fontsize=20)
        plt.savefig(psi5_jpg_1_path, dpi=300, bbox_inches="tight")

    def test_solve_2(self):
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic() +\
                            hamiltonian.operator_external()

        eig_vals_mat, eig_psis_mat = \
                        Solver.solve(hamiltonian_matrix)
        print(eig_vals_mat.shape)
        print(eig_psis_mat.shape)

        # 绘图
        plt.figure(figsize=(10, 8))
        for idx in range(5):
            plt.plot(xs_lst, eig_psis_mat[:, idx])
        plt.xlabel("1D coordination", fontsize=20)
        plt.ylabel("Psi", fontsize=20)
        plt.savefig(psi5_jpg_2_path, dpi=300, bbox_inches="tight")


    def test_solve_3(self):
        hamiltonian = Hamiltonian(xs_lst=xs_lst)
        hamiltonian_matrix = hamiltonian.operator_kenitic() +\
                            hamiltonian.operator_well()

        eig_vals_mat, eig_psis_mat = \
                        Solver.solve(hamiltonian_matrix)
        print(eig_vals_mat.shape)
        print(eig_psis_mat.shape)

        # 绘图
        plt.figure(figsize=(10, 8))
        for idx in range(5):
            plt.plot(xs_lst, eig_psis_mat[:, idx])
        plt.xlabel("1D coordination", fontsize=20)
        plt.ylabel("Psi", fontsize=20)
        plt.savefig(psi5_jpg_3_path, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    unittest.main()