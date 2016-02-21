import numpy as np
from pyhdf.SD import SD, SDC, SDS
import sys


_file = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD35\MOD35_L2.A2015220.0215.006.2015220134621.hdf'
mod35 = SD(_file, SDC.READ)


#List SDS

ds = mod35.datasets()
ds_lst = ds.keys()

for i in range(len(ds_lst)):
	print ds_lst[i]
	print "\n"

sds_name = "Cloud_Mask"
sds = mod35.select(sds_name)

data = sds.attributes(full=1)
print data['description']


mod35.end()