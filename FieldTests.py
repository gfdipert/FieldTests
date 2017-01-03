import csv

class FieldTests(object):

	def __init__(self,csvfile):
		self.reader = csv.DictReader(csvfile)
		self.Fieldname = 'name/__text'
		self.Fieldtype = 'fieldType/__text'
		self.Contextual = 'contextualField/__text'
		self.Partneredit = 'partnerEditable/__text'
		self.Otherpers = 'otherDisplayOption/__text'
		self.Values = 'values/__text'
		self.Defaultvals = 'defaults/__text'
		self.Default = 'toIgnorePartnerDefaults/__text'
		self.Marcom = 'availableToMarcom/__text'

	def completefieldtest(self,fieldname,fieldtype,contextual,partneredit,otherpers,default,marcom,values=None,defaultvals=None):

		for row in self.reader:
			if fieldname == row[self.Fieldname]:
				if row[self.Fieldtype] != fieldtype:
					print "Field type for {0} is {1} and should be {2}".format(fieldname,row[self.Fieldtype],fieldtype)
				if row[self.Contextual] != contextual:
					print "Contextual value for {0} is {1} and should be {2}".format(fieldname,row[self.Contextual],contextual)
				if row[self.Partneredit] != partneredit:
					print "Partner editability for {0} is {1} and should be {2}".format(fieldname,row[self.Partneredit],partneredit)
				if row[self.Otherpers] != otherpers:
					print "Other personalization for {0} is {1} and should be {2}".format(fieldname,row[self.Otherpers],otherpers)
				if row[self.Default] != default:
					print "Skip partner default setting for {0} is {1} and should be {2}".format(fieldname,row[self.Default],default)
				if row[self.Marcom] != marcom:
					print "Marcom setting for {0} is {1} and should be {2}".format(fieldname,row[self.Marcom],marcom)

				if values != None:
					if row[self.Values] != values:
						print "All values for {0} are {1} and should be {2}".format(fieldname,row[self.Values],values)
				if defaultvals != None:
					if row[self.Defaultvals] != defaultvals:
						print "All default values for {0} is {1} and should be {2}".format(fieldname,row[self.Defaultvals],values)


	def typetest(self,list,value):

		for row in self.reader:
			if row[self.Fieldname] in list:
				if row[self.fFieldtype] != value:
					print row[self.Fieldname] + " is not " + value

	def valuetest(self,fieldname,key,value):

		for row in self.reader:
			if fieldname == row[self.Fieldname]:
				if row[key] == value:
					print "The setting is correct."
				else:
					print "The " + key + " value for " + fieldname + " is not " + value .format(key,fieldname,value)

	def listallfields(self,key,value):

		for row in self.reader:
			if (key,value) in row.iteritems():
				print row[self.fieldname]

	def listallattributes(self,fieldname):

		for row in self.reader:
			if fieldname == row[self.Fieldname]:
				print "Field type: " + row[self.Fieldtype]
				print "Contextual: " + row[self.Contextual]
				print "Partner Editable: " + row[self.Partneredit]
				print "Other personalization: " + row[self.Otherpers]
				print "Values: " + row[self.Values]
				print "Default Values: " + row[self.Defaultvals]
				print "Skip partner defaulting: " + row[self.Default]
				print "Viewable in Marcom: " + row[self.Marcom]
