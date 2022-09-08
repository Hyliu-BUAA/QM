'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-08 21:48:47
LastEditTime : 2022-09-08 21:51:02
FilePath     : /Quantum_Mechanics/DFT/test.py
Description  : 
'''
from ase.dft.kpoints import monkhorst_pack, get_monkhorst_pack_size_and_offset

print( monkhorst_pack((4, 2, 1)) )
print( get_monkhorst_pack_size_and_offset([[0, 0, 0]]) )