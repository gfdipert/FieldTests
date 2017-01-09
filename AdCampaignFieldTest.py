"""
excel formula 
=CONCATENATE("completefieldtest(",A2,B2,C2,",",C2,D2,E2,",",E2,F2,G2,",",G2,H2,I2,",",I2,J2,K2,",",K2,L2,M2,",",M2,N2,O2,",",O2,P2,Q2,",",Q2,R2,S2,")")
"""

from FieldTests import FieldTests
CSV = raw_input('Enter CSV file name: ')

with open(CSV) as csvfile:
	test = FieldTests(csvfile)
	test.completefieldtest("Ads","channellist","false","true","false","false","true")
	test.completefieldtest("Panel CSS","richtext","true","false","false","true","false")
	test.completefieldtest("Email Validation","radio","false","true","false","false","true")
	test.completefieldtest("Email JS","richtext","true","false","false","true","false")
	test.completefieldtest("Partner Display Name","edit","false","true","false","false","true")
	test.completefieldtest("Logo","embeddedimage","false","true","false","false","true")
	test.completefieldtest("Partner Phone","edit","false","true","false","false","true")
	test.completefieldtest("Primary Color","colorpicker","false","true","false","false","true")
	test.completefieldtest("Secondary Color","colorpicker","false","true","false","false","true")
	test.completefieldtest("Partner Value Proposition","richtext","false","true","false","false","true")
	test.completefieldtest("Partner URL","url","false","true","false","false","true")
	test.completefieldtest("Privacy Option","radio","false","true","false","false","true")
	test.completefieldtest("Privacy URL","url","false","true","false","false","true")
	test.completefieldtest("Terms Option","radio","false","true","false","false","true")
	test.completefieldtest("Terms URL","url","false","true","false","false","true")
	test.completefieldtest("Partner Subhead","edit","false","true","false","false","true")
	test.completefieldtest("Inline Address","edit","false","true","false","false","true")
	test.completefieldtest("Sender Email","edit","false","true","false","false","true")
	test.completefieldtest("Sender Display Name","edit","false","true","false","false","true")
	test.completefieldtest("Ads 123","channellist","false","true","false","false","false","true")