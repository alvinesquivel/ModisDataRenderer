import numpy as np
from pyhdf.SD import SD, SDC
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys


_filename = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
sds_name = 'Cloud_Top_Temperature'
mod06 = SD(_filename, SDC.READ)
sds_index = mod06.select(sds_name)
sds_index_data = sds_index.get()



fig = plt.figure()
ax = fig.add_subplot(111)
cmap = plt.cm.nipy_spectral
bounds = np.arange(0, 301, 20)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
sds_index_data = sds_index_data * 0.01
img = plt.imshow(np.flipud(sds_index_data), vmin = 0.0, vmax = 300.0, cmap = cmap, interpolation = 'nearest', origin = 'lower')
cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = bounds, ticks = bounds)
cbar.set_label("Kelvin")
plt.title('MODIS L2 CLOUD TOP TEMPERATURE', fontsize = 10)
plt.show()
