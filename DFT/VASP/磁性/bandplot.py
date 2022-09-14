import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter

bs_vasprun = Vasprun("./vasprun.xml",parse_projected_eigen=False)
bs_data = bs_vasprun.get_band_structure(line_mode=True)

band_fig = BSPlotter(bs=bs_data)
band_fig.get_plot(ylim=(-1,1))
plt.savefig('band_fig.png')


