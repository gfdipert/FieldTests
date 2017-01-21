import os

from FieldTests2CSV import FieldTests
refcsvinput = raw_input('Enter reference CSV file name: ')
csvinput = raw_input('Enter CSV file you would like to check: ')

with open(CSV) as csvfile:
    with open(REFCSV) as refcsvfile:
		test = FieldTests(csvfile,refcsvfile)
		test.refcompletefieldtest()
		#test.newfields()
		#test.defaultvalsprint()
