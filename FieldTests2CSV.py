import csv

class FieldTests(object):

	def __init__(self,csvfile,refcsvfile):

		#parse testing CSV file
		self.reader = csv.DictReader(csvfile)
		self.rows = []
		for row in self.reader:
			self.rows.append(row)

		#parse reference CSV file
		self.refreader = csv.DictReader(refcsvfile)
		self.refrows = []
		for refrow in self.refreader:
			self.refrows.append(refrow)

		self.Fieldname = 'name/__text'
		self.Fieldtype = 'fieldType/__text'
		self.Contextual = 'contextualField/__text'
		self.Partneredit = 'partnerEditable/__text'
		self.Otherpers = 'otherDisplayOption/__text'
		self.Values = 'values/__text'
		self.Defaultvals = 'defaults/__text'
		self.Default = 'toIgnorePartnerDefaults/__text'
		self.Marcom = 'availableToMarcom/__text'

	def refcompletefieldtest(self):
		for row in self.rows:
			for refrow in self.refrows:
				if refrow[self.Fieldname] == row[self.Fieldname]:
					if refrow[self.Fieldtype] != row[self.Fieldtype]:
						print "Field type for {0} is {1} and should be {2}".format(refrow[self.Fieldname],row[self.Fieldtype],refrow[self.Fieldtype])
					elif refrow[self.Contextual] != row[self.Contextual]:
						print "Contextual value for {0} is {1} and should be {2}".format(refrow[self.Fieldname],row[self.Contextual],refrow[self.Contextual])
					elif refrow[self.Partneredit] != row[self.Partneredit]:
						print "Partner editability for {0} is {1} and should be {2}".format(refrow[self.Fieldname],row[self.Partneredit],refrow[self.Partneredit])
					elif refrow[self.Otherpers] != row[self.Otherpers]:
						print "Other personalization for {0} is {1} and should be {2}".format(refrow[self.Fieldname],row[self.Otherpers],refrow[self.Otherpers])
					elif refrow[self.Default] != row[self.Default]:
						print "Skip partner defaulting for {0} is {1} and should be {2}".format(refrow[self.Fieldname],row[self.Default],refrow[self.Default])
					elif refrow[self.Marcom] != row[self.Marcom]:
						print "Viewable in Marcom for {0} is {1} and should be {2}".format(refrow[self.Fieldname],row[self.Marcom],refrow[self.Marcom])
			#add condition that lists all unknown fields