import os
import glob
import os.path
from FieldTests2CSV import FieldTests


csvs = []

"""
def csvimport(file,list):
	os.chdir(file)
	for counter, files in enumerate(glob.glob("*.csv")):
		list.append(files)

csvimport("MarcomLanding/",csvs)


for folder in os.listdir("."):
	print folder
	for file in folder:
		print file
		if file.endswith('.csv'):
			csvs.append(file)
"""


for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".csv")]:
        os.path.join(dirpath,f)



"""
def walk(dir,meth):
	dir = os.path.abspath(dir)
	for file in [file for file in os.listdir(dir) if file.endswith(".csv")]:
		nfile = os.path.join(dir,file)
		meth(nfile)
		if os.path.isdir(nfile):
			self.walk(nfile,meth)
walk(".",meth)
"""


REFCSV = raw_input('Enter reference CSV file name: ')
CSV = raw_input('Enter CSV file you would like to check: ')

with open(CSV) as csvfile:
	with open(REFCSV) as refcsvfile:
		test = FieldTests(csvfile,refcsvfile)
		test.refcompletefieldtest()
		test.newfields()
		#test.defaultvalsprint()
