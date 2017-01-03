from FieldTests import FieldTests

#desired values for field types
checkbox = ['Email Options','Sidebar Options','Social Icons']

colorpicker = ['Accent Color','Accent CTA Color']

contextual = ['Preheader', 'Logo and Contact', 'Banner', 'Body with Sidebar', 'Body without Sidebar', 'PVP', 'Partner Address with Social', 'Footer', 'Footer Code', 'Landing Page Footer Code']

email = ['Partner Email']

image = ['Logo','Banner Image','Sidebar Image','Landing Page Image']

radio = ['Greeting Options','Signature Option','Privacy Policy Option','Terms and Conditions Option','Landing Page Image Option','CTA Link Option']

simpletext = ['Subject','View Online','Partner Display Name','Partner Phone','Partner URL Text','Banner Image Alt','Title','Greeting Text','First Name Field','Body Copy CTA','Sidebar CTA','Landing Page Headline','Confirmation Page Headline','Confirmation Button CTA','Secondary Body CTA','Inline Address']

url = ['Asset URL','Secondary Asset URL','Partner URL','Twitter URL','Facebook URL','LinkedIn URL','Google URL','YouTube URL','RSS URL','Privacy Policy URL','Terms and Conditions URL']

CSV = raw_input('Enter CSV file name: ')

#nicknames of attributes
contextual = 'contextualField/__text'
partneredit = 'partnerEditable/__text'
otherpers = 'otherDisplayOption/__text'
values = 'values/__text'
defaultvals = 'defaults/__text'
default = 'toIgnorePartnerDefaults/__text'
marcom = 'availableToMarcom/__text'

"""
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

"""
with open(CSV) as csvfile:
	test = FieldTests(csvfile)
	test.completefieldtest('Email Options','checkbox','FALSE','TRUE','FALSE','FALSE','TRUE')

