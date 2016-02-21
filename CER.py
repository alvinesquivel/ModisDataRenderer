from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import sys

_file = 'F:\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
mod06 =SD(_file, SDC.READ)
sds = mod06.select('Cloud_Effective_Radius')
sds_data = sds.get()


print sds_data

fig = plt.figure()
ax = fig.add_subplot(111)
cmap = plt.cm.Spectral
bounds = [0, 25, 50]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
sds_data = sds_data * 0.01
img = plt.imshow(np.fliplr(sds_data), vmin = 0, vmax = 50, cmap = cmap, interpolation = 'none', origin = 'lower')
plt.title('MODIS L2 CLOUD EFFECTIVE RADIUS', fontsize = 10)
plt.show()