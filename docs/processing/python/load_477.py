#load_477.py - load 477 data by state
#mike byrne
#may 18, 2020

#variables and importing
import psycopg2
import time
import json
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

#schema/prefix/workorder/projection
sch = "form_477_201906"
inDir = "/Users/mike/Documents/Data/fcc/477_2019_06/v1/"
fileSuffix = "-Fixed-Jun2019-v1.csv"
#
#******************************************************
#						FUNCTIONS 
#******************************************************
#	
#create the output table
def initOutput(myST):
	aST = myST[0]
	aFIPS = myST[1]
	myTab = "fcc_477_" + aFIPS
	mySQL = "DROP TABLE IF EXISTS " + sch + "." + myTab 
	mySQL = mySQL + " ; COMMIT; "
	mkCur.execute(mySQL)
	mySQL = "CREATE TABLE " + sch + "." + myTab + " ("
	mySQL = mySQL + "logrecno character varying(10), "
	mySQL = mySQL + "provider_id character varying(10), "
	mySQL = mySQL + "frn character varying(10), "
	mySQL = mySQL + "providername character varying(225), "
	mySQL = mySQL + "dbaname character varying(225), "
	mySQL = mySQL + "holdingcompanyname character varying(225), "
	mySQL = mySQL + "hoconum integer,"
	mySQL = mySQL + "hocofinal character varying(225), "
	mySQL = mySQL + "stateabbr character varying(2), "
	mySQL = mySQL + "blockcode character varying(15), "
	mySQL = mySQL + "techcode integer, "
	mySQL = mySQL + "consumer integer, "
	mySQL = mySQL + "maxaddown numeric, "
	mySQL = mySQL + "maxadup numeric, "
	mySQL = mySQL + "business integer, "
	mySQL = mySQL + "maxcirdown numeric, "
	mySQL = mySQL + "maxcirup numeric "
	mySQL = mySQL + ") WITH (OIDS = FALSE) ;"

	#print mySQL
	#CREATE TABLE data.fcc_477_20171231_05 (logrecno character varying(10), 
	#provider_id character varying(10), frn character varying(10), 
	#providername character varying(225), dbaname character varying(225), 
	#holdingcompanyname character varying(225), hoconum integer,
	#hocofinal character varying(225), stateabbr character varying(2), 
	#blockcode character varying(15), techcode integer, consumer integer, 
	#maxaddown numeric, maxadup numeric, business integer, 
	#maxcirdown numeric, maxcirup numeric ) WITH (OIDS = TRUE) 
	#TABLESPACE pg_default;
	mkCur.execute(mySQL)

	mySQL = "COPY " + sch + "." + myTab + " "
	mySQL = mySQL + "FROM '" + inDir + aST + fileSuffix + "' CSV HEADER; "
	#print mySQL
	#COPY data.fcc_477_20171231_04 
	#FROM '/Users/mike/Documents/Data/FCC/477_20171231/raw/AZ-Fixed-Dec2017-v1.csv' 
	#CSV HEADER; 
	mkCur.execute(mySQL)


#add a comment for the shape
def addComment(myST):
	aST = myST[0]
	aFIPS = myST[1]	
	myTab = "fcc_477_" + aFIPS

	myComment = myTab + ": "
	myComment = myComment + "Table added on: " + str(time.asctime(now)) + ". "
	myComment = myComment + "Data source directory is: " + inDir + ". "
	myComment = myComment + "Data source file is: " + aST + fileSuffix + ". "

	mySQL = "COMMENT ON TABLE " + sch + "." + myTab + " "
	mySQL = mySQL + "IS '" + myComment + "'; "
	mySQL = mySQL + "COMMIT; "
	#print mySQL
	#COMMENT ON TABLE forked_deer.substations IS 
	#'Table added on: Mon Jul  2 22:14:47 2018. 
	#Data source directory is: /Users/mike/documents/data/conex/input/forked_deer/source/20180627/DISTIBUTIONSOURCE/. 
	#Data source file is: DISTIBUTIONSOURSES.shp. '; COMMIT;
	mkCur.execute(mySQL)


#perform the vaccum
def myVacuum(myST):
	aST = myST[0]
	aFIPS = myST[1]	
	myTab = "fcc_477_" + aFIPS
	vConn = psycopg2.connect(myConn)
	# #aCur
	aCur = vConn.cursor()
	old_isolation_level = vConn.isolation_level
	vConn.set_isolation_level(0)
	print "			vaccuming: " + sch + "." + myTab	
	mySQL = "VACUUM ANALYZE " + sch + "." + myTab + "; "
	aCur.execute(mySQL)
	vConn.set_isolation_level(old_isolation_level)
	# #clean up
	aCur.close()

#
#******************************************************
#						MAIN 
#******************************************************
#	
conn = psycopg2.connect(myConn)
#make cursor - used to make a new table
mkCur = conn.cursor()

myList = [
		["AK","02"],["AL","01"],["AZ","04"],["AR","05"],["CA","06"],["CO","08"],["CT","09"],
		["DE","10"],["DC","11"],["FL","12"],["GA","13"],["HI","15"],["ID","16"],["IL","17"],
		["IN","18"],["IA","19"],["KS","20"],["KY","21"],["LA","22"],
		["ME", "23"],["MD","24"],["MA","25"],["MI","26"],["MN","27"],["MS","28"],["MO","29"],["MT","30"],
		["NE", "31"],["NV","32"],["NH","33"],["NJ","34"],["NM","35"],["NY","36"],["NC","37"],["ND","38"],
		["OH", "39"],["OK","40"],["OR","41"],["PA","42"],["RI","44"],["SC","45"],["SD","46"], 
		["TN","47"],["TX","48"],["UT","49"],["VT","50"],["VA", "51"],
		["WA","53"],["WV","54"],["WI","55"],["WY","56"],
		["AS","60"],["GU","66"],["MP","69"],["VI","78"] #["PR","72"],
		]

for myST in myList:
	print "...doing..." + myST[0]
	initOutput(myST)
	addComment(myST)
	myVacuum(myST)

#clean up
mkCur.close()

#end
print "		finished: " + (__file__)
now = time.localtime(time.time())
print "end time:", time.asctime(now)
