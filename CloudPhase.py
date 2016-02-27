from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import sys

#Read HDF Files

MOD06_FILE_NAME = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
mod06 = SD(MOD06_FILE_NAME, SDC.READ)
mod06_sds = mod06.select('Cloud_Phase_Optical_Properties')
mod06_sds_data = mod06_sds.get()
print type(mod06_sds_data)
print ("HDF file loaded")


fig = plt.figure()
ax = fig.add_subplot(111)
cmap = plt.cm.gist_earth
bounds = [2, 3, 4, 5]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
mod06_sds_data = mod06_sds_data + 0.5
img = plt.imshow(np.fliplr(mod06_sds_data), vmin = 2.0, vmax = 5.0, cmap = cmap, interpolation = 'nearest',
                 origin = 'lower')
cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = bounds, ticks = [2.5, 3.5, 4.5])
cbar.ax.set_yticklabels([ 'Liquid', 'Ice', 'Undetermined \n Cloud Phase' ], fontsize=10)
ax.set_xlabel("", fontsize=7)
ax.set_ylabel("", fontsize=1)
plt.title('MODIS L2 Cloud Phase Discrimination', fontsize=10)
plt.show()
