import os
import glob
from FieldTests2CSV import FieldTests

csvs = []
#csvnames = []

for root,dirs,files in os.walk("./"):
	for file in files:
		if file.endswith((".csv")):
			csvs.append(file)

refcsvinput = raw_input('Enter reference CSV file name: ')
csvinput = raw_input('Enter CSV file you would like to check: ')

for file in csvs:
	if refcsvinput == file:
		REFCSV = file
	if csvinput == file:
		CSV = file

with open(CSV) as csvfile:
    with open(REFCSV) as refcsvfile:
		test = FieldTests(csvfile,refcsvfile)
		test.refcompletefieldtest()
		#test.newfields()
		#test.defaultvalsprint()
