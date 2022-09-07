'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-07 17:41:16
LastEditTime : 2022-09-07 17:47:33
FilePath     : /Quantum_Mechanics/DFT/1D_DFT/code/test/test_selfConvergence.py
Description  : 
'''
import unittest
import numpy as np
import matplotlib.pyplot as plt

# python3 -m code.test.test_selfConvergence
from ..driver.hamiltonian import Hamiltonian
from ..driver.solver import Solver
from ..driver.densityCalculator import DensityCalculator
from ..driver.selfConsistency import SelfConsistence


num_grids = 201
xs_lst = np.linspace(-5, 5, num_grids)
num_electrons = 17
max_iters = 1000
energy_tolerence = 1e-5
densitys_array = np.zeros(num_grids)


class SelfConsistenceTest(unittest.TestCase):
    def test_run(self):
        scf = SelfConsistence(
            xs_lst=xs_lst,
            num_electrons=num_electrons,
            max_iters=max_iters,
            energy_tolerence=energy_tolerence,
            eps=1e-1
            )
        scf.run(densitys_array=densitys_array)



if __name__ == "__main__":
    unittest.main()