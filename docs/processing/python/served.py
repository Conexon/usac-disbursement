#served.py
#mike byrne
#may 18, 2020

#sets up an individual state block data
#that is joined to the 477 data


#with associated flag fields for each 
#	- cable 
#	- fiber



#variables and importing
import os
from subprocess import call
import psycopg2
import time
now = time.localtime(time.time())
print "start time:", time.asctime(now)
print "	begin: " + (__file__)

#
#******************************************************
#						VARIABLES
#******************************************************
#
#connection
myDB = "fcc" 
myHost = "localhost"
myPort = "5432"
myUser = "" 
myPWord = ""
myConn = "dbname=" + myDB + " host=" + myHost + " port=" + myPort + " user=" + myUser + " password=" + myPWord
FNULL = open(os.devnull, 'w')

#schema/prefix/workorder/projection
sch = "form_477_201906" #"fcc" #"form_477_201712"

#tables
#input 
blPre = "block_"
blSuf = "_2018"
fccPre = "fcc_477_"


#block fields
blBlFld = "geoid10"

#477 fields
hocoFld = "provider_id"
fccBlFld = "blockcode"
fccTFld = "techcode"
fccDownFld = "maxaddown"
fccUpFld = "maxadup"

#
#******************************************************
#						FUNCTIONS 
#******************************************************
#	
#create the output table
def initOutput(myFips, myField):
	#myFips = myST[1]
	#aST = myST[0]
	myTB = blPre + myFips + blSuf
	mySQL = "ALTER TABLE " + sch + "." + myTB + " DROP COLUMN IF EXISTS "
	mySQL = mySQL + myField + "; "
	#print mySQL
	#ALTER TABLE form_477_201712.block_44_2018 DROP COLUMN IF EXISTS has_speed; 
	mkCur.execute(mySQL)
	mySQL = "ALTER TABLE " + sch + "." + myTB + " ADD COLUMN "
	mySQL = mySQL + myField + " INTEGER ; "
	#print mySQL
	#ALTER TABLE form_477_201712.block_44_2018 ADD COLUMN has_speed INTEGER ; 
	mkCur.execute(mySQL)

#do the analysis
def singleField(myFips, aField, initField):
	myFips = myST[1]
	aST = myST[0]
	myBLTB = blPre + myFips + blSuf
	myFCCTB = fccPre + myFips

	print "		initiating: " + aField
	if initField == 1:
		initOutput(myFips, aField)
	if aField == "cable":							#(4)
		myWhere = fccTFld + " in (40,41,42,43) and consumer = 1 "
	if aField == "fiber":							#(6)
		myWhere = fccTFld + " in (50) and consumer = 1 "
	
	updField(myBLTB, myFCCTB, aField, myWhere)

#update the field
def updField(blkTB, fccTB, aField, aWhere):
	#update block table from working table
	updSQL = "UPDATE " + sch + "." + blkTB + " SET " + aField + "=1 "
	updSQL = updSQL + "FROM " + sch + "." + fccTB + " "
	updSQL = updSQL + "WHERE " + blBlFld + "=" + fccBlFld + " AND "
	updSQL = updSQL + aWhere + "; COMMIT; " 
	# print updSQL
	#UPDATE form_477_201712.block_29_2018 
	#	SET unserved=1 
	#	FROM form_477_201712.fcc_477_29 
	#	WHERE geoid10=blockcode 
	#	AND has_speed = 0 
	#	AND docsis = 0 
	#	and fiber = 0 ; 
	#	COMMIT;	
	updCur.execute(updSQL)

	# # #set other fields = 0
	mySQL = "UPDATE " + sch + "." + blkTB + " SET " + aField + "=0 "
	mySQL = mySQL + "WHERE " + aField + " IS NULL; COMMIT; "
	# print mySQL
	#UPDATE form_477_201712.block_29_2018 
	#	SET unserved=0 
	#	WHERE unserved IS NULL; 
	#	COMMIT;  
	mkCur.execute(mySQL)
	myVacuum(sch, blkTB)

#perform the vaccum
def myVacuum(mySch, myTB):
	vConn = psycopg2.connect(myConn)
	#aCur
	aCur = vConn.cursor()
	old_isolation_level = vConn.isolation_level
	vConn.set_isolation_level(0)
	print "			vaccuming: " + mySch + "." + myTB
	mySQL = "VACUUM ANALYZE " + mySch + "." + myTB + "; "
	aCur.execute(mySQL)
	vConn.set_isolation_level(old_isolation_level)
	#clean up
	aCur.close()





#
#******************************************************
#						MAIN 
#******************************************************
#	
conn = psycopg2.connect(myConn)
#a select cursor
aCur = conn.cursor()
#insCur 
insCur	 = conn.cursor()
#updCuror
updCur = conn.cursor()
#make cursor - used to make a new table
mkCur = conn.cursor()


myList = [
	["AL","01"],["AK","02"],["AZ","04"],["AR","05"],["CA","06"],["CO","08"],["CT","09"], 
	["DE","10"],["DC","11"],["FL","12"],["GA","13"],["HI","15"],["ID","16"],["IL","17"], 
	["IN","18"],["IA","19"],["KS","20"],["KY","21"],["LA","22"], 
	["ME","23"],["MD","24"],["MA","25"],["MI","26"],["MN","27"],["MS","28"],["MO","29"],["MT","30"], 
	["NE","31"],["NV","32"],["NH","33"],["NJ","34"],["NM","35"],["NC","37"],["ND","38"],["NY","36"], 
	["OH","39"],["OK","40"],["OR","41"],["PA","42"],["RI","44"],["SC","45"],["SD","46"],  
	["TN","47"],["TX","48"],["UT","49"],["VT","50"],["VA", "51"],  
	["WA","53"],["WV","54"],["WI","55"],["WY","56"],  
	# ["AS","60"],["GU","66"],["MP","69"],["VI","78"], #["PR","72"]
		]


#for the coop_boundaries data
for myST in myList:
	print "	starting: " + myST[0]
	#need to do is_fast, then not_fast
	fieldList = ["cable","fiber"]
	for field in fieldList:
	 	singleField(myST,field,1)
#clean up
aCur.close()
insCur.close()
updCur.close()
mkCur.close()

#end
print "		finished: " + (__file__)
now = time.localtime(time.time())
print "end time:", time.asctime(now)
