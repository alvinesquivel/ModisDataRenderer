from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import sys

_file = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
mod06 =SD(_file, SDC.READ)
sds = mod06.select('Cloud_Effective_Radius')
sds_data = sds.get()

for x in np.nditer(sds_data, op_flags = ['readwrite']):
	if (x[...] == -9999):
		x[...] = 0


#print sds_data

fig = plt.figure()
ax = fig.add_subplot(111)
cmap = plt.cm.nipy_spectral
bounds = np.arange(5, 66, 10)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
sds_data = sds_data * 0.01
img = plt.imshow(np.flipud(sds_data), vmin = 0, vmax = 60.0, cmap = cmap, interpolation = 'none', origin = 'lower')
cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = bounds, ticks = bounds)
cbar.set_label("microns")
plt.title('MODIS L2 CLOUD EFFECTIVE RADIUS', fontsize = 10)
plt.show()