from FieldTests import FieldTests

CSV = raw_input('Enter CSV file name: ')

#nicknames of attributes
contextual = 'contextualField/__text'
partneredit = 'partnerEditable/__text'
otherpers = 'otherDisplayOption/__text'
values = 'values/__text'
defaultvals = 'defaults/__text'
default = 'toIgnorePartnerDefaults/__text'
marcom = 'availableToMarcom/__text'

#all fields that are simple text
with open(CSV) as csvfile:     
	test = FieldTests(csvfile)
	test.typetest(simpletext,'edit')

#all fields that are contextual
with open(CSV) as csvfile:     
	test = FieldTests(csvfile)
	test.listallfields(contextual,'TRUE')

#all attributes for a single field
with open(CSV) as csvfile:     
	test = FieldTests(csvfile)
	test.listallattributes('Body with Sidebar')

#whether desired settings are in place
with open(CSV) as csvfile:
	test = FieldTests(csvfile)
	test.valuetest('Social Icons',partneredit,'TRUE')

with open(CSV) as csvfile:
	test = FieldTests(csvfile)
	test.listallattributes('Subject')


with open(CSV) as csvfile:
	test = FieldTests(csvfile)
	test.completefieldtest('Email Options','checkbox','FALSE','TRUE','FALSE','FALSE','TRUE','blah','blah')

"""
excel formula 

w/ values and defaults
=CONCATENATE("test.completefieldtest(",A2,B2,C2,",",C2,D2,E2,",",E2,F2,G2,",",G2,H2,I2,",",I2,J2,K2,",",K2,L2,M2,",",M2,N2,O2,",",O2,P2,Q2,",",Q2,R2,S2,")")

w/o
=CONCATENATE("test.completefieldtest(",A2,B2,C2,",",C2,D2,E2,",",E2,F2,G2,",",G2,H2,I2,",",I2,J2,K2,",",K2,L2,M2,",",M2,N2,O2,")")


"""

