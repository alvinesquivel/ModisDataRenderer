import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pyhdf.SD import *
import sys

#np.set_printoptions(threshold='nan')


_filename = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD35\MOD35_L2.A2015348.0215.006.2015348134053.hdf'
mod35 = SD(_filename, SDC.READ)

sds_name_cm = 'Cloud_Mask'

sds_index_cm = mod35.select(sds_name_cm)
cm_sds_data = sds_index_cm.get()






sds_data_0 = cm_sds_data[0, :, :]
sds_data_0_bin = sds_data_0.astype(dtype=np.uint8, order='K', casting='unsafe', subok=False, copy=False)


for x in np.nditer(sds_data_0_bin, op_flags=['readwrite']):
	x[...] = np.right_shift(x, 6)



fig = plt.figure()
ax = fig.add_subplot(111)



cmap = plt.cm.brg
bounds = [0, 1, 2, 3]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
img = plt.imshow(np.flipud(sds_data_0_bin), vmin = 0, vmax = 3, cmap = cmap, interpolation = 'nearest',
	origin = 'lower')
cbar = plt.colorbar(img, cmap = cmap, norm = norm, boundaries = bounds, ticks = [1, 2, 3])
cbar.ax.set_yticklabels(['Coastal', 'Desert', 'Land'], fontsize=10)
ax.set_xlabel("", fontsize=7)
ax.set_ylabel("", fontsize=1)
plt.title('Cloud Mask - Land Water Flag', fontsize = 10)
plt.show()



#y = np.empty_like(sds_data_0)
#for x in sds_data_0:
#	print sds_data_0[x]
#	print type(sds_data_0[x])
#	break
#print type(sds_data_0[0,0])
#print sds_data_0[0,0]
#sds_data_0_bin = np.binary_repr(sds_data_0, width=8)
#x = np.right_shift(sds_data_0[0,0], 6)
#print x
#x_rs = np.binary_repr(x, width=2)
#print x_rs

#Bit packing
#y = np.empty_like(sds_data_0)
#z = y.astype(np.uint8)
#z[0,0] = x_rs
#z[0,0] = z[0,0] - 8
#print z[0,0]
#i = np.unpackbits(z[0,0])
#print i
#j = np.packbits(i)
#print j
#x = BitArray(int=sds_data_0[2029,1339], length=8)
#xstr = x.bin



#print np.shape(sds_data_0)
#print sds_data_0[0,0]

#for x in sds_data_0:
	#print sds_data_0[0]

	#sds_data_0_bin[x] = BitArray(int=sds_data_0[x], length=8)

#print x.bin