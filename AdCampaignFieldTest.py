"""
excel formula 
=CONCATENATE("completefieldtest(",A2,B2,C2,",",C2,D2,E2,",",E2,F2,G2,",",G2,H2,I2,",",I2,J2,K2,",",K2,L2,M2,",",M2,N2,O2,",",O2,P2,Q2,",",Q2,R2,S2,")")
"""

from FieldTests import FieldTests
CSV = raw_input('Enter CSV file name: ')

with open(CSV) as csvfile:
	test = FieldTests(csvfile)
	test.completefieldtest("Ads","channellist","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Panel CSS","richtext","TRUE","FALSE","FALSE","TRUE","FALSE")
	test.completefieldtest("Email Validation","radio","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Email JS","richtext","TRUE","FALSE","FALSE","TRUE","FALSE")
	test.completefieldtest("Partner Display Name","edit","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Logo","embeddedimage","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Partner Phone","edit","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Primary Color","colorpicker","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Secondary Color","colorpicker","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Partner Value Proposition","richtext","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Partner URL","url","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Privacy Option","radio","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Privacy URL","url","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Terms Option","radio","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Terms URL","url","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Partner Subhead","edit","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Inline Address","edit","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Sender Email","edit","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Sender Display Name","edit","FALSE","TRUE","FALSE","FALSE","TRUE")
	test.completefieldtest("Ads 123","channellist","FALSE","TRUE","FALSE","FALSE","FALSE","TRUE")