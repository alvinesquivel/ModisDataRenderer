import numpy as np
from pyhdf.SD import SD, SDC
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

_filename = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD35\MOD35_L2.A2015348.0215.006.2015348134053.hdf'
mod35 = SD(_filename, SDC.READ)
mod35_lat = mod35.select('Latitude')
mod35_lon = mod35.select('Longitude')
mod35_lat_data = mod35_lat.get()
mod35_lon_data = mod35_lon.get()

print mod35_lat_data.shape
print mod35_lon_data.shape

ArrayShape = mod35_lat_data.shape
as0 = ArrayShape[0] - 1
as1 = ArrayShape[1] - 1

latmin = mod35_lat_data[0,0]
latmax = mod35_lat_data[as0,as1]

lat_0 = latmin + (latmax - latmin) / 2

print lat_0

tmp0 = mod35_lon_data[0,0]
tmp1 = mod35_lon_data[as0, as1]

lonmin = min(tmp0, tmp1)
lonmax = max(tmp0, tmp1)

lon_0 = lonmin + (lonmax - lonmin) / 2

print lon_0

if lon_0 > 180:
	lon_0 = - (360 - lon_0)

mod35_lon_data[0,0] = tmp0
mod35_lon_data[as0,as1] = tmp1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor('white')
m1 = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = None)
xpt0, ypt0 = m1(lon_0, lat_0)
xpt1, ypt1 = m1(mod35_lon_data[0,0], mod35_lat_data[0,0])
xpt2, ypt2 = m1(mod35_lon_data[0,as1], mod35_lat_data[0,as1])
xpt3, ypt3 = m1(mod35_lon_data[as0, as1], mod35_lat_data[as0,as1])
xpt4, ypt4 = m1(mod35_lon_data[as0, 0], mod35_lat_data[as0,0])

llx = min(xpt1, xpt2, xpt3, xpt4) - xpt0
lly = min(ypt1, ypt2, ypt3, ypt4) - ypt0
urx = max(xpt1, xpt2, xpt3, xpt4) - xpt0
ury = max(ypt1, ypt2, ypt3, ypt4) - ypt0

m = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', llcrnrx = llx, llcrnry = lly, urcrnrx = urx, urcrnry = ury)
lon = mod35_lon_data
lat = mod35_lat_data
x_igrid, y_igrid = m(lon, lat)


#m.drawcoastlines()
#plt.show()






