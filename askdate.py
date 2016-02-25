import datetime

inp_date = raw_input("Enter date (YYYY.MM.DD): ")


mod06 = "MOD06_L2.AYYYYDDD.HHMM.VVV.YYYYDDDHHMMSS.hdf"
mod35 = "MOD35_L2.AYYYYDDD.HHMM.VVV.YYYYDDDHHMMSS.hdf"

date_format = '%Y.%m.%d'
date = datetime.datetime.strptime(inp_date, date_format)
print date