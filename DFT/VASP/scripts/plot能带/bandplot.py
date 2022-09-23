'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-14 15:14:27
LastEditTime : 2022-09-16 11:48:27
FilePath     : /Quantum_Mechanics/DFT/VASP/scripts/plot能带/bandplot.py
Description  : 
'''
import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter


bs_vasprun = Vasprun("./vasprun.xml",parse_projected_eigen=False)
bs_data = bs_vasprun.get_band_structure(line_mode=True)

band_fig = BSPlotter(bs=bs_data)
band_fig.get_plot(ylim=(-2,2))
plt.savefig('band_fig.png')