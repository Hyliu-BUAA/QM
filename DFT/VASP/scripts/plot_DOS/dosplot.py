'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-15 10:16:06
LastEditTime : 2022-09-15 10:17:31
FilePath     : /Quantum_Mechanics/DFT/VASP/scripts/plot_DOS/dosplot.py
Description  : 
'''
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import DosPlotter

# 2. Automated workflow
vasprun_path = './vasprun.xml'

pic_path = "./dsplot.png"
# read vasprun.xml，get band and dos information
dos_vasprun=Vasprun(vasprun_path)
dos_data=dos_vasprun.complete_dos

# set figure parameters, draw figure
plotter = DosPlotter()
plotter.add_dos('total dos', dos_data)
plotter.add_dos_dict(dos_data.get_element_dos())
print(dos_data.get_element_dos())
plotter.get_plot(xlim=(-2, 2))
plt.savefig(pic_path)
