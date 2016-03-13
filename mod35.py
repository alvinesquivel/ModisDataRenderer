import numpy as np
from pyhdf.SD import SD, SDC
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

_filename = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD35\MOD35_L2.A2012004.0215.006.2015055131835.hdf'
_filename1 = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD03\MOD03.A2012004.0215.006.2012285090648.hdf'
#_filename2 = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
mod35 = SD(_filename, SDC.READ)
mod03 = SD(_filename1, SDC.READ)
#mod06 = SD(_filename2, SDC.READ)
mod03_lat = mod03.select('Latitude')
mod03_lon = mod03.select('Longitude')
mod03_lat_data = mod03_lat.get()
mod03_lon_data = mod03_lon.get()
mod35_sds = mod35.select('Cloud_Mask')
#mod06_sds = mod06.select('Cloud_Optical_Thickness')



print mod03_lat_data.shape
print mod03_lon_data.shape

ArrayShape = mod03_lat_data.shape
as0 = ArrayShape[0] - 1
as1 = ArrayShape[1] - 1

latmin = mod03_lat_data[0,0]
latmax = mod03_lat_data[as0,as1]

lat_0 = latmin + (latmax - latmin) / 2

print lat_0

tmp0 = mod03_lon_data[0,0]
tmp1 = mod03_lon_data[as0, as1]

lonmin = min(tmp0, tmp1)
lonmax = max(tmp0, tmp1)

lon_0 = lonmin + (lonmax - lonmin) / 2

print lon_0

if lon_0 > 180:
	lon_0 = - (360 - lon_0)

mod03_lon_data[0,0] = tmp0
mod03_lon_data[as0,as1] = tmp1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor('white')
def format_coord(x, y):
	return 'Longitude={:6.3f}\nLatitude={:6.3f}\nPixel value:'.format(x, y)
ax.format_coord = format_coord
m1 = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = None)
xpt0, ypt0 = m1(lon_0, lat_0)
xpt1, ypt1 = m1(mod03_lon_data[0,0], mod03_lat_data[0,0])
xpt2, ypt2 = m1(mod03_lon_data[0,as1], mod03_lat_data[0,as1])
xpt3, ypt3 = m1(mod03_lon_data[as0, as1], mod03_lat_data[as0,as1])
xpt4, ypt4 = m1(mod03_lon_data[as0, 0], mod03_lat_data[as0,0])

llx = min(xpt1, xpt2, xpt3, xpt4) - xpt0
lly = min(ypt1, ypt2, ypt3, ypt4) - ypt0
urx = max(xpt1, xpt2, xpt3, xpt4) - xpt0
ury = max(ypt1, ypt2, ypt3, ypt4) - ypt0

m = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', llcrnrx = llx, llcrnry = lly, urcrnrx = urx, urcrnry = ury)
lon = mod03_lon_data
lat = mod03_lat_data
x_igrid, y_igrid = m(lon, lat)
x_igrid = x_igrid - xpt0
y_igrid = y_igrid - ypt0
#mod06_sds_data = mod06_sds.get()
#print mod06_sds_data.dtype
#print mod06_sds_data.shape
sds_data = mod35_sds.get()
sds_data_0 = sds_data[0, :, :]
sds_data_0_bin = sds_data_0.astype(dtype = np.uint8, order = 'K', casting = 'unsafe', subok = False, copy = False)

for x in np.nditer(sds_data_0_bin, op_flags = ['readwrite']):
	x[...] = np.right_shift(x, 6)

for y in np.nditer(sds_data_0_bin, op_flags = ['readwrite']):
	if (y[...] == 3 or y[...] == 2):
		y[...] = 0

#sds_data_0_bin_int16 =  sds_data_0_bin.astype(dtype = np.int16, order = 'K', casting = 'unsafe', subok = False, copy = False)
z_igrid = sds_data_0_bin
#print z_igrid[0,0]

#for i in np.nditer(sds_data_0_bin_int16, op_flags = ['readwrite']):
#	for j in np.nditer(mod06_sds_data):
#		k = j
#	if (i[...] == 0):
#		i[...] = k
#	print i
x1_igrid = x_igrid.ravel()
y1_igrid = y_igrid.ravel()
#z1_igrid = z_igrid.ravel()
xy1_igrid = np.vstack((x1_igrid, y1_igrid)).T
cmap = plt.cm.gnuplot2
bounds = np.arange(0, 2, 1)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
img = m.imshow(np.flipud(z_igrid), origin = 'lower', vmin = 0.0, vmax = 1.0, cmap = cmap)
#m.drawcoastlines()
m.drawparallels(np.arange(-90.,120.,5.), color='w', labels=[True,False,False,False])
m.drawmeridians(np.arange(115.,360.,5.), color='w', labels=[False,False,False,True])


plt.title("Map")
plt.show()






