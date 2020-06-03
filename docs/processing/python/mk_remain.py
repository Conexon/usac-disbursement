#mk_remain.py
#mike byrne
#may 18, 2020

#makes the remaining area polygons outside SAC

#variables and importing
import os
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
sch = "usac" 
dSch = "data"

#tables
#input 
statesTB = "states"
sacTB = "sac"
outTB = "remain"


#initate the output table
def initiateFinalTB():
	mkSQL = "DROP TABLE IF EXISTS " + sch + "." + outTB + "_final; COMMIT; "
	mkSQL = mkSQL + "CREATE TABLE " + sch + "." + outTB + "_final ( "
	mkSQL = mkSQL + "state_abbv character varying(2), "
	mkSQL = mkSQL + "geom geometry(Polygon,4269)"
	mkSQL = mkSQL + ") "
	mkSQL = mkSQL + "; COMMIT; "
	# print (mkSQL)
	#DROP TABLE IF EXISTS usac.remain; COMMIT; 
	#CREATE TABLE usac.remain 
	#	( 
	#	state_abbv character varying(2), 
	#	geom geometry(MultiPolygon,4269)
	#	) ; 
	# COMMIT; 
	mkCur.execute(mkSQL)

	mySQL = "ALTER TABLE " + sch + "." + outTB + "_final ADD COLUMN gid serial not null; "
	# print (mySQL)
	# ALTER TABLE usac.remain ADD COLUMN gid serial not null; 
	updCur.execute(mySQL)

def insertFinal(myST):
	insSQL = "INSERT INTO " + sch + "." + outTB + "_final (state_abbv, geom) "
	insSQL = insSQL + "SELECT '" + myST + "', (ST_Dump(ST_SimplifyPreserveTopology(geom, 0.001))).geom "
	insSQL = insSQL + "FROM " + sch + "." + outTB + " "
	insSQL = insSQL + "WHERE state_abbv = '" + myST + "' "
	insSQL = insSQL + "; COMMIT; "
	# print (insSQL)
	#INSERT INTO usac.remain 
	#	(state_abbv, geom) 
	#	SELECT 'MS', geom 
	#	FROM data.states 
	#	WHERE stusps = 'MS' ; 
	# COMMIT;
	insCur.execute(insSQL)
	delSQL = "DELETE FROM " + sch + "." + outTB + "_final "
	delSQL = delSQL + "WHERE st_area(geom) / st_perimeter(geom) < 0.001; "
	# print (delSQL)
	# DELETE FROM usac.remain_final 
	#	WHERE st_area(geom) / st_perimeter(geom) < 0.001; 
	insCur.execute(delSQL)

#initate the output table
def initiateTB():
	mkSQL = "DROP TABLE IF EXISTS " + sch + "." + outTB + "; COMMIT; "
	mkSQL = mkSQL + "CREATE TABLE " + sch + "." + outTB + " ( "
	mkSQL = mkSQL + "state_abbv character varying(2), "
	mkSQL = mkSQL + "geom geometry(MultiPolygon,4269)"
	mkSQL = mkSQL + ") "
	mkSQL = mkSQL + "; COMMIT; "
	# print (mkSQL)
	#DROP TABLE IF EXISTS usac.remain; COMMIT; 
	#CREATE TABLE usac.remain 
	#	( 
	#	state_abbv character varying(2), 
	#	geom geometry(MultiPolygon,4269)
	#	) ; 
	# COMMIT; 
	mkCur.execute(mkSQL)

	mySQL = "ALTER TABLE " + sch + "." + outTB + " ADD COLUMN gid serial not null; "
	# print (mySQL)
	# ALTER TABLE usac.remain ADD COLUMN gid serial not null; 
	updCur.execute(mySQL)


#insert the state polygon
def insertStatePoly(myST):
	insSQL = "INSERT INTO " + sch + "." + outTB + " (state_abbv, geom) "
	insSQL = insSQL + "SELECT '" + myST + "', geom "
	insSQL = insSQL + "FROM " + dSch + "." + statesTB + " "
	insSQL = insSQL + "WHERE stusps = '" + myST + "' "
	insSQL = insSQL + "; COMMIT; "
	# print (insSQL)
	#INSERT INTO usac.remain 
	#	(state_abbv, geom) 
	#	SELECT 'MS', geom 
	#	FROM data.states 
	#	WHERE stusps = 'MS' ; 
	# COMMIT;
	insCur.execute(insSQL)

#update the polygon with the difference of each polygon
def driveDifferene(aST):
	driveCur = conn.cursor()
	myST = aST[0]
	myFIPS = aST[1]
	driveSQL = "SELECT gid from " + sch + "." + sacTB + " "
	driveSQL = driveSQL + "WHERE state_abbv = '" + myST + "' "
	driveSQL = driveSQL + "ORDER by gid "
	# driveSQL = driveSQL + "limit 1"
	driveSQL = driveSQL + "; "
	# print (driveSQL)
	# SELECT gid from usac.sac 
	#	WHERE state_abbv = 'MS' 
	#	ORDER by gid; 
	driveCur.execute(driveSQL)
	for row in driveCur:
		# print (row[0])
		aGID = str(row[0])
		if aGID <> '3562' :
			updDifference(myST, aGID)
	driveCur.close()


#now update the exisint polygon with the difference
def updDifference(aST, aGID):
	updSQL = "UPDATE " + sch + "." + outTB + " "
	updSQL = updSQL + "SET geom = "
	updSQL = updSQL + "(SELECT ST_Multi(ST_Difference(states.geom, "
	updSQL = updSQL + "ST_Transform(sac.geom, 4269)) )"
	updSQL = updSQL + "FROM " + sch + "." + outTB + " as states, "
	updSQL = updSQL + "(SELECT geom from " + sch + "." + sacTB + " "
	updSQL = updSQL + "WHERE gid =" + str(aGID) + ") as sac " 
	updSQL = updSQL + "WHERE state_abbv = '" + aST + "' "
	updSQL = updSQL + ") "
	updSQL = updSQL + "WHERE state_abbv = '" + aST + "' "
	# updSQL = updSQL + "AND ST_Intersects(geom, " + outTB + ".geom) "
	updSQL = updSQL + "; "
	updSQL = updSQL + "COMMIT; "
	# print (updSQL)
	# UPDATE usac.remain 
	# 	SET geom = 
	# 	(SELECT ST_Difference(states.geom, ST_Transform(sac.geom, 4269)) 
	# 	FROM usac.remain as states, 
	# 	(SELECT geom from usac.sac WHERE gid =2395) as sac 
	# 	WHERE state_abbv = 'MS') 
	# 	;
	# COMMIT;
	updCur.execute(updSQL)
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
	["AL","01"],["AK","02"],["AZ","04"],["AR","05"],["CA","06"],["CO","08"],["CT","09"], #A
	["DE","10"],["DC","11"],["FL","12"],["GA","13"],["HI","15"],["ID","16"],["IL","17"], #B
	["IN","18"],["IA","19"],["KS","20"],["KY","21"],["LA","22"], #C
	["ME","23"],["MD","24"],["MA","25"],["MI","26"],["MN","27"],["MS","28"],["MO","29"],["MT","30"], #D
	["NE","31"],["NV","32"],["NH","33"],["NJ","34"],["NM","35"],["NC","37"],["ND","38"],["NY","36"], #E
	["OH","39"],["OK","40"],["OR","41"],["PA","42"],["RI","44"],["SC","45"],["SD","46"],  #F
	["TN","47"],["TX","48"],["UT","49"],["VT","50"],["VA", "51"],  #G
	["WA","53"],["WV","54"],["WI","55"],["WY","56"]
		]

initiateTB()
initiateFinalTB()

# #for the coop_boundaries data
for myST in myList:
	print "	starting: " + myST[0]
	insertStatePoly(myST[0])
	driveDifferene(myST)
	insertFinal(myST[0])

#clean up
aCur.close()
insCur.close()
updCur.close()
mkCur.close()
