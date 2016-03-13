import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pyhdf.SD import *
import sys

#np.set_printoptions(threshold='nan')

_filename = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD35\MOD35_L2.A2015348.0215.006.2015348134053.hdf'
mod35 = SD(_filename, SDC.READ)


sds_name='Cloud_Mask'
sds_index = mod35.select(sds_name)
sds_data = sds_index.get()


sds_data_0 = sds_data[0, :, :]
sds_data_0_bin = sds_data_0.astype(dtype=np.uint8, order='K', casting='unsafe', subok=False, copy=False)

#print sds_data_0_bin[0,0]
#print np.binary_repr(sds_data_0_bin[0,0], width=8)
#x = np.right_shift(sds_data_0_bin[0,0], 1)
#print x
#print np.binary_repr(x, width=8) #original data


#x_int8 = np.uint8(x)
#y = np.left_shift(x_int8, 6)
#print y
#print np.binary_repr(y, width=8) #after shifting 6 bits to right (16 bits width)

#y_int8 = np.uint8(y)
#print y_int8
#print np.binary_repr(y_int8, width=8) #after shifting 6 bits to the right (8 bits)

#z = np.right_shift(y_int8, 6) #expexted data (8 bits)
#print z

for x in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
	x[...] = np.right_shift(x, 1)

for y in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
	y[...] = np.left_shift(y, 6)

for z in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
	z[...] = np.right_shift(z, 6)

fig = plt.figure()
ax = fig.add_subplot(111)
cmap = plt.cm.YlGn
bounds = np.arange(0, 4, 1)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
img = plt.imshow(np.flipud(sds_data_0_bin), vmin = 0, vmax = 3, cmap = cmap, interpolation = 'nearest',
	origin = 'lower')
cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = None, ticks = bounds)
cbar.ax.set_yticklabels(['Confident Cloudy', 'Probably Cloudy', 'Probably Clear', 'Confident Clear'], fontsize = 10)
ax.set_xlabel("", fontsize = 7)
ax.set_ylabel("", fontsize = 1)
plt.title("Cloud Mask - Unobstructed FOV Quality", fontsize = 10)
plt.show()



