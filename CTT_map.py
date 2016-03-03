import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from pyhdf.SD import SD, SDC
from mpl_toolkits.basemap import Basemap, cm
from scipy import interpolate
from scipy.interpolate import griddata

#Read HDF Files

MOD06_FILE_NAME = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
MOD03_FILE_NAME = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD03\MOD03.A2015188.0215.006.2015188145151.hdf'
mod06 = SD(MOD06_FILE_NAME, SDC.READ)
mod03 = SD(MOD03_FILE_NAME, SDC.READ)
mod03_Latitude = mod06.select('Latitude')
mod03_Longitude = mod06.select('Longitude')
mod06_sds = mod06.select('Cloud_Top_Temperature')
mod03_Latitude_data = mod03_Latitude.get()
mod03_Longitude_data = mod03_Longitude.get()
mod06_sds_data = mod06_sds.get()

print "Read hdf done"

#Find lat_0 and lon_0

print mod03_Latitude_data.shape
print mod03_Longitude_data.shape
ArrayShape = mod03_Latitude_data.shape
as0 = ArrayShape[0] - 1
as1 = ArrayShape[1] - 1
latmin = mod03_Latitude_data[0,0]
latmax = mod03_Latitude_data[as0,as1]
lat_0 = latmin + (latmax - latmin) / 2
print "lat_0: ", lat_0

tmp_01 = mod03_Longitude_data[0,0]
tmp_02 = mod03_Longitude_data[as0,as1]
lonmin = min(mod03_Longitude_data[0,0],mod03_Longitude_data[as0,as1])
lonmax = max(mod03_Longitude_data[0,0],mod03_Longitude_data[as0,as1])
lon_0 = lonmin + (lonmax -lonmin) / 2

if lon_0 > 180:
    lon_0 = - (360 - lon_0)
mod03_Longitude_data[0,0] = tmp_01
mod03_Longitude_data[as0,as1] = tmp_02

print latmin, latmax
print lonmin, lonmax
print "lat_0 and lon_0 done"


#Orthographic map
fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor('white')
m1 = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution=None)
xpt0, ypt0 = m1(lon_0,lat_0)
xpt1, ypt1 = m1(mod03_Longitude_data[0,0],mod03_Latitude_data[0,0])
xpt2, ypt2 = m1(mod03_Longitude_data[0,as1],mod03_Latitude_data[0,as1])
xpt3, ypt3 = m1(mod03_Longitude_data[as0,as1], mod03_Latitude_data[as0,as1])
xpt4, ypt4 = m1(mod03_Longitude_data[as0,0],mod03_Latitude_data[as0,0])
llx = min(xpt1,xpt2,xpt3,xpt4) - xpt0
lly = min(ypt1,ypt2,ypt3,ypt4) - ypt0
urx = max(xpt1,xpt2,xpt3,xpt4) - xpt0
ury = max(ypt1,ypt2,ypt3,ypt4) - ypt0

m = Basemap(projection='ortho',lon_0=lon_0,lat_0=lat_0,resolution='l',\
            llcrnrx=llx,llcrnry=lly,urcrnrx=urx,urcrnry=ury)
print "Orthographic map done"

#Plot MODIS data
lon = mod03_Longitude.get()
lat = mod03_Latitude.get()
x_igrid, y_igrid = m(lon,lat)
x_igrid = x_igrid - xpt0
y_igrid = y_igrid - ypt0
z_igrid = mod06_sds.get()
z_igrid = z_igrid * 0.01
x1_igrid = x_igrid.ravel()
y1_igrid = y_igrid.ravel()
z1_igrid = z_igrid.ravel()
xy1_igrid = np.vstack((x1_igrid,y1_igrid)).T
xi, yi = np.mgrid[llx:urx:1000j, lly:ury:1000j]
z = griddata(xy1_igrid, z1_igrid, (xi, yi), method='cubic')
cmap = plt.cm.nipy_spectral
#mpl.colors.ListedColormap(['k', '0.55', '#0D0575', '#C9CDEC', '#CBC206'])
bounds = np.arange(0, 301, 20)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
img = m.imshow(z.T, vmin = 0.0, vmax=300.0, cmap=cmap, interpolation = 'nearest', origin='lower')
cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds)
cbar.set_label("Kelvin (K)")
#cbar.ax.set_yticklabels(bounds, fontsize=10)
m.drawcoastlines()
m.drawparallels(np.arange(-90.,120.,5.), color='w', labels=[True,False,False,False])
m.drawmeridians(np.arange(115.,360.,5.), color='w', labels=[False,False,False,True])
ax.set_xlabel("", fontsize=10)
ax.set_ylabel("", fontsize=10)
plt.title('MODIS L2 Cloud Top Temperature', fontsize=10)
plt.show()
