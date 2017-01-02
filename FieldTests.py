import csv

class FieldTests(object):

	def __init__(self,csvfile):
		self.reader = csv.DictReader(csvfile)
		self.fieldname = 'name/__text'
		self.fieldtype = 'fieldType/__text'
		self.contextual = 'contextualField/__text'
		self.partneredit = 'partnerEditable/__text'
		self.otherpers = 'otherDisplayOption/__text'
		self.values = 'values/__text'
		self.defaultvals = 'defaults/__text'
		self.default = 'toIgnorePartnerDefaults/__text'
		self.marcom = 'availableToMarcom/__text'

	def typetest(self,list,value):

		for row in self.reader:
			if row[self.fieldname] in list:
				if row[self.fieldtype] != value:
					print row[self.fieldname] + " is not " + value

	def valuetest(self,fieldname,key,value):

		for row in self.reader:
			if fieldname == row[self.fieldname]:
				if row[key] == value:
					print "The setting is correct."
				else:
					print "The " + key + " value for " + fieldname + " is not " + value

	def listallvalues(self,key,value):

		for row in self.reader:
			if (key,value) in row.iteritems():
				print row[self.fieldname]

	def listallattributes(self,fieldname):

		for row in self.reader:
			if fieldname == row[self.fieldname]:
				print "Field type: " + row[self.fieldtype]
				print "Contextual: " + row[self.contextual]
				print "Partner Editable: " + row[self.partneredit]
				print "Other personalization: " + row[self.otherpers]
				print "Values: " + row[self.values]
				print "Default Values: " + row[self.defaultvals]
				print "Skip partner defaulting: " + row[self.default]
				print "Viewable in Marcom: " + row[self.marcom]
