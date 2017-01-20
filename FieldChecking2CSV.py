import os

#results += [each for each in os.listdir('/Users/gwendipert/Documents/Field\ Validation/CYO') if each.endswith('.csv')]

from FieldTests2CSV import FieldTests
REFCSV = raw_input('Enter reference CSV file name: ')
CSV = raw_input('Enter CSV file you would like to check: ')

with open(CSV) as csvfile:
    with open(REFCSV) as refcsvfile:
		test = FieldTests(csvfile,refcsvfile)
		#test.refcompletefieldtest()
		test.newfields()
		#test.defaultvalsprint()
