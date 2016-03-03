import numpy as np
from pyhdf.SD import SD, SDC
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

_filename = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
mod06 = SD(_filename, SDC.READ)
sds_name = 'Cloud_Water_Path'
sds_index = mod06.select(sds_name)
sds_index_data = sds_index.get()

for x in np.nditer(sds_index_data, op_flags = ['readwrite']):
	if (x[...] == -9999):
		x[...] = 0




fig = plt.figure()
ax = fig.add_subplot(111)
cmap = plt.cm.nipy_spectral
bounds = np.arange(0, 61, 10)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
sds_index_data = sds_index_data * 0.01
img = plt.imshow(np.flipud(sds_index_data), vmin = 0.0, vmax = 60, cmap = cmap, interpolation = 'nearest', origin = 'lower')
cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = bounds, ticks = bounds)
cbar.set_label("g/m2")
plt.title('MODIS L2 Cloud Water Path')
plt.show()