import csv

class FieldTests(object):

	def __init__(self,csvfile,refcsvfile):

		self.Fieldname = 'name/__text'
		self.Fieldtype = 'fieldType/__text'
		self.Contextual = 'contextualField/__text'
		self.Partneredit = 'partnerEditable/__text'
		self.Otherpers = 'otherDisplayOption/__text'
		self.Values = 'values/__text'
		self.Defaultvals = 'defaults/__text'
		self.Ignore = 'toIgnorePartnerDefaults/__text'
		self.Marcom = 'availableToMarcom/__text'

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

		#creates list of ref CSV field names
		self.refnames = []
		for refrow in self.refrows:
			self.refnames.append(refrow[self.Fieldname])

		#creates list of CSV field names
		self.names = []
		for row in self.rows:
			self.names.append(row[self.Fieldname])

		#creates list of values if field is not contextual
		self.defaultvals = {}
		for row in self.rows:
			if row[self.Contextual] != "true":
				self.defaultvals[row[self.Fieldname]] = row[self.Defaultvals]

	def refcompletefieldtest(self):
		for row in self.rows:
			for refrow in self.refrows:
				if refrow[self.Fieldname] == row[self.Fieldname]:
					if refrow[self.Fieldtype] != row[self.Fieldtype]:
						print "Field type for {0} is {1} and should be {2}".format(row[self.Fieldname],row[self.Fieldtype],refrow[self.Fieldtype])
					if refrow[self.Contextual] != row[self.Contextual]:							
						print "Contextual value for {0} is {1} and should be {2}".format(row[self.Fieldname],row[self.Contextual],refrow[self.Contextual])
					if refrow[self.Partneredit] != row[self.Partneredit]:
						print "Partner editability for {0} is {1} and should be {2}".format(row[self.Fieldname],row[self.Partneredit],refrow[self.Partneredit])
					if refrow[self.Otherpers] != row[self.Otherpers]:
						print "Other personalization for {0} is {1} and should be {2}".format(row[self.Fieldname],row[self.Otherpers],refrow[self.Otherpers])
					if refrow[self.Ignore] != row[self.Ignore]:
						print "Skip partner defaulting for {0} is {1} and should be {2}".format(row[self.Fieldname],row[self.Ignore],refrow[self.Ignore])
					if refrow[self.Marcom] != row[self.Marcom]:
						print "Viewable in Marcom for {0} is {1} and should be {2}".format(row[self.Fieldname],row[self.Marcom],refrow[self.Marcom])

	def newfields(self):
		missingfields = []
		for fieldname in self.names:
			if fieldname not in self.refnames:
				missingfields.append(fieldname)
		print "This is a list of fields being used in your CSV that aren't in the Reference CSV:"
		print missingfields


	def defaultvalsprint(self):
		print "Here are the default values for the non-contextual fields:"
		for key in self.defaultvals:
			if self.defaultvals[key] == "":
				pass
			else:
				print "{0} : {1}".format(key,self.defaultvals[key])


