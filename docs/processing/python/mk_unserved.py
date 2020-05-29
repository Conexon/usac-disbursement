#mk_unserved.py
#mike byrne
#may 18, 2020

#make a dissolved map of each states' unserved

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
myDB = "fcc" # "tn_grant" #fcc
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


#dissolve the layer
def dissolveTB(myST):
	myState = myST[0].lower()
	myFIPS = myST[1]
	myInTb = "block_" + myFIPS + "_2018"
	myTB = "unserved_" + myState 
	mySQL = "DROP TABLE IF EXISTS " + sch + "." + myTB + "; "
	mySQL = mySQL + "CREATE TABLE " + sch + "." + myTB + " AS "
	mySQL = mySQL + "SELECT statefp10, (st_dump(ST_SimplifyPreserveTopology(st_union(geom), 0.001))).geom as geom "
	mySQL = mySQL + "FROM " + sch + "." + myInTb + " "
	mySQL = mySQL + "WHERE (fiber = 0 and cable = 0) "
	mySQL = mySQL + "AND aland10 > awater10 "
	mySQL = mySQL + "GROUP BY statefp10 "
	mySQL = mySQL + "; "
	mySQL = mySQL + "COMMIT; "
	# print (mySQL)
	# DROP TABLE IF EXISTS form_477_201906.unserved_de; 
	# CREATE TABLE form_477_201906.unserved_de AS 
	#	SELECT statefp10, (st_dump(ST_SimplifyPreserveTopology(st_union(geom), 0.001))).geom as geom 
	#	FROM form_477_201906.block_10_2018 
	#	WHERE has_25_3 = 0 
	#	AND aland10 > awater10 
	#	GROUP BY statefp10 ; 
	#	COMMIT; 
	mkCur.execute(mySQL)

	#now update to add on appropriate columns etc
	mySQL = "ALTER TABLE " + sch + "." + myTB + " ADD COLUMN gid serial not null; COMMIT; "
	# print (mySQL)
	# ALTER TABLE form_477_201906.unserved_de ADD COLUMN gid serial not null; 
	updCur.execute(mySQL) 

	mySQL = "ALTER TABLE " + sch + "." + myTB + " add constraint blocks_unserved_" 
	mySQL = mySQL + myState + "_pkey primary key (gid); COMMIT;  "
	# print (mySQL)
	# ALTER TABLE form_477_201906.unserved_de add constraint blocks_unserved_de_pkey_gid primary key (gid);
	updCur.execute(mySQL)
	mySQL = "ALTER TABLE " + sch + "." + myTB + " "
	mySQL = mySQL + "ALTER COLUMN geom TYPE geometry(Polygon, 4269) "
	mySQL = mySQL + "USING ST_SetSRID(geom,4269); COMMIT; "
	# print (mySQL)
	# ALTER TABLE form_477_201906.unserved_de 
	#	ALTER COLUMN geom TYPE geometry(Polygon, 4269) 
	#	USING ST_SetSRID(geom,4269); COMMIT; 
	updCur.execute(mySQL)

	myVacuum(sch, myTB)


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
	["ME","23"],["NH","33"],["VT","50"],["NY","36"],["MA","25"],["CT","09"], #region_1
		["RI","44"],["PA","42"],["NJ","34"],["DE","10"],["MD","24"],
	["DC","11"],["WV","54"],["VA", "51"],["KY","21"],["TN","47"],["NC","37"],#region_2
		["MS","28"],["AL","01"],["GA","13"],["SC","45"],["FL","12"],	
	["OH","39"],["IN","18"],["IL","17"],["IA","19"],["MI","26"],["WI","55"], #region_3
		["MN","27"],
	["TX","48"],["OK","40"],["KS","20"],["MO","29"],["AR","05"],["LA","22"], #region_4
	["MT","30"],["ND","38"],["SD","46"],["WY","56"],["NE","31"],["CO","08"], #region_5
		["UT","49"],["AZ","04"],["NM","35"],
	["WA","53"],["OR","41"],["ID","16"],["CA","06"],["NV","32"],["HI","15"], #region_6
		["AK","02"]
	]


#for the coop_boundaries data
for myST in myList:
	print "	starting: " + myST[0]
	dissolveTB(myST)

#clean up
aCur.close()
insCur.close()
updCur.close()
mkCur.close()

#end
print "		finished: " + (__file__)
now = time.localtime(time.time())
print "end time:", time.asctime(now)
