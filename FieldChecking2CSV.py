import os
import glob
import sys
from FieldTests2CSV import FieldTests

directories = [os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name)]

csvpaths = []

refcsvinputname = raw_input('Enter reference CSV file name: ')
csvinputname = raw_input('Enter CSV file you would like to check: ')

for directory in directories:
	refpathname = os.path.join(directory,refcsvinputname)
	csvpathname = os.path.join(directory,csvinputname)
	filenames = os.listdir(directory)
	for filename in filenames:
		pathname = os.path.join(directory,filename)
		if refpathname == pathname:
			REFCSV = refpathname
		if csvpathname == pathname:
			CSV = csvpathname

print REFCSV
print CSV

with open(CSV) as csvfile:
    with open(REFCSV) as refcsvfile:
    	test = FieldTests(csvfile,refcsvfile)
		test.refcompletefieldtest()
		#test.newfields()
		#test.defaultvalsprint()
