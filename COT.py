from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import sys


_file = 'E:\School Files\Special Problem\MODIS\MOD06\MOD06_L2.A2015188.0215.006.2015190003732.hdf'
mod06 = SD(_file, SDC.READ)
sds = mod06.select('Cloud_Optical_Thickness')
sds_data = sds.get()


print sds_data

fig = plt.figure()
ax = fig.add_subplot(111)
cmap = plt.cm.gist_earth
bounds = [25, 50, 75, 100, 125, 150]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
sds_data = sds_data * 0.01
img = plt.imshow(np.fliplr(sds_data), vmin = 25.0, vmax = 150.0, cmap = cmap, interpolation = 'nearest', origin = 'lower')
plt.title('MODIS L2 Cloud Optical Thickness', fontsize=10)
plt.show()