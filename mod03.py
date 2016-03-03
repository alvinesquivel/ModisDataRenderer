import numpy as np
from pyhdf.SD import SD, SDC
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap



_filename = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD03\MOD03.A2015188.0215.006.2015188145151.hdf'
#filename1 = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'

#mod06 = SD(_filename1, SDC.READ)
#mod06_sds = mod06.select('Cloud_Optical_Thickness')
mod03 = SD(_filename, SDC.READ)
mod03_lat = mod03.select('Latitude')
mod03_lon = mod03.select('Longitude')

#mod06_sds_data = mod06_sds.get()
mod03_lat_data = mod03_lat.get()
mod03_lon_data = mod03_lon.get()


print mod03_lat_data.shape
print mod03_lon_data.shape

ArrayShape = mod03_lat_data.shape
as0 = ArrayShape[0] - 1
as1 = ArrayShape[1] - 1

latmin = mod03_lat_data[0,0]
latmax = mod03_lat_data[as0, as1]

lat_0 = latmin + (latmax - latmin) / 2

print lat_0

tmp0 = mod03_lon_data[0,0]
tmp1 = mod03_lon_data[as0,as1]
lonmin = min(tmp0,tmp1)
lonmax = max(tmp0,tmp1)

lon_0 = lonmin + (lonmax - lonmin) / 2

print lon_0

if lon_0 > 180:
	lon_0 = - (360 - lon_0)

mod03_lon_data[0,0] = tmp0
mod03_lon_data[as0, as1] = tmp1


fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor('white')
m1 = Basemap(projection = 'ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = None)
xpt0, ypt0 = m1(lon_0,lat_0)
xpt1, ypt1 = m1(mod03_lon_data[0,0], mod03_lat_data[0,0])
xpt2, ypt2 = m1(mod03_lon_data[0, as1], mod03_lat_data[0,as1])
xpt3, ypt3 = m1(mod03_lon_data[as0, as1], mod03_lat_data[as0, as1])
xpt4, ypt4 = m1(mod03_lon_data[as0, 0], mod03_lat_data[as0, 0])
llx = min(xpt1,xpt2,xpt3,xpt4) - xpt0
lly = min(ypt1,ypt2,ypt3,ypt4) - ypt0
urx = max(xpt1,xpt2,xpt3,xpt4) - xpt0
ury = max(ypt1,ypt2,ypt3,ypt4) - ypt0

m = Basemap(projection ='ortho', lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', llcrnrx = llx, llcrnry = lly, urcrnrx = urx, urcrnry = ury)
#lon = mod3_lon.get()
#lat = mod03_lat.get()
m.drawcoastlines()
plt.show()
