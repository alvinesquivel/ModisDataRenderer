import numpy as np
from pyhdf.SD import SD, SDC, SDS
import sys



_file = 'C:\Users\AKO NA LNG\Desktop\Esquivel Files\School Files 2\Special Problem\MODIS\MOD06\MOD06_L2.A2015348.0215.006.2015348152515.hdf'
mod06 = SD(_file, SDC.READ)



#List SDS


ds = mod06.datasets()
ds_lst = ds.keys()

for i in range(len(ds_lst)):
	print ds_lst[i]



#Metadata for Cloud Optical Thickness
sds_name = "Cloud_Optical_Thickness"
sds = mod06.select(sds_name)

data = sds.attributes(full=1)
data_keys_lst = data.keys()
print "\n"
print "**************************************\n"
print "CLOUD OPTICAL THICKNESS METADATA\n"
print "======================================\n"
for key in data_keys_lst:
	print key + ":"
	print data[key]
	print "\n"
print "=======================================\n"



mod06.end()

