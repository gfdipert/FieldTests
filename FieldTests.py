import csv

class FieldTests(object):

	def __init__(self,csvfile):

		#parse testing CSV file
		self.reader = csv.DictReader(csvfile)
		self.rows = []
		for row in self.reader:
			self.rows.append(row)
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

		for row in self.rows:
			if fieldname == row[self.Fieldname]:
				if row[self.Fieldtype] != fieldtype:
					print "Field type for {0} is {1} and should be {2}".format(fieldname,row[self.Fieldtype],fieldtype)
				elif row[self.Contextual] != contextual:
					print "Contextual value for {0} is {1} and should be {2}".format(fieldname,row[self.Contextual],contextual)
				elif row[self.Partneredit] != partneredit:
					print "Partner editability for {0} is {1} and should be {2}".format(fieldname,row[self.Partneredit],partneredit)
				elif row[self.Otherpers] != otherpers:
					print "Other personalization for {0} is {1} and should be {2}".format(fieldname,row[self.Otherpers],otherpers)
				elif row[self.Default] != default:
					print "Skip partner default setting for {0} is {1} and should be {2}".format(fieldname,row[self.Default],default)
				elif row[self.Marcom] != marcom:
					print "Marcom setting for {0} is {1} and should be {2}".format(fieldname,row[self.Marcom],marcom)
				
				"""if row[self.Values] != "None":
					if row[self.Values] != values:
						print "Value(s) for {0} are {1} and should be {2}".format(fieldname,row[self.Values],values)
				if row[self.Defaultvals] != "None":
					if row[self.Defaultvals] != defaultvals:
						print "Default value(s) for {0} is {1} and should be {2}".format(fieldname,row[self.Defaultvals],defaultvals)
				"""

	def typetest(self,list,value):

		for row in self.reader:
			if row[self.Fieldname] in list:
				if row[self.fFieldtype] != value:
					print "{0} is not {1}".format(row[self.Fieldname],value)

	def valuetest(self,fieldname,key,value):

		for row in self.reader:
			if fieldname == row[self.Fieldname]:
				if row[key] == value:
					print "The setting is correct."
				else:
					print "The {0} value for {1} is not {2}".format(key,fieldname,value)

	def listallfields(self,key,value):

		for row in self.reader:
			if (key,value) in row.iteritems():
				print row[self.fieldname]

	def listallattributes(self,fieldname):

		for row in self.reader:
			if fieldname == row[self.Fieldname]:
				print "Field type: {0}".format(row[self.Fieldtype])
				print "Contextual: {0}".format(row[self.Contextual])
				print "Partner Editable: {0}".format(row[self.Partneredit])
				print "Other personalization: {0}".format(row[self.Otherpers])
				print "Values: {0}".format(row[self.Values])
				print "Default Values: {0}".format(row[self.Defaultvals])
				print "Skip partner defaulting: {0}".format(row[self.Default])
				print "Viewable in Marcom: {0}".format(row[self.Marcom])
