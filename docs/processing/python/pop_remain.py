#mk_remain.py
#mike byrne
#makes the remaining area polygons outside SAC
#may 18, 2020

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

#tables
#input 
outTB = "remain"
sacTB = "sac"
disTB = "disbursement"


#initate the output table
def initFields():
	fields = ["unacc_hc", "unacc_caf", "total", "num_sac"]
	for field in fields:		
		updSQL = "ALTER TABLE " + sch + "." + outTB + " "
		updSQL = updSQL + "DROP COLUMN IF EXISTS " + field + " "
		updSQL = updSQL + "; COMMIT; "
		updSQL = updSQL + "ALTER TABLE " + sch + "." + outTB + " "
		if field == "num_sac":
			myType = "integer"
		else:
			myType = "money" 
		updSQL = updSQL + "ADD COLUMN " + field + " " + myType + " "
		updSQL = updSQL + "; COMMIT; "
		# print (updSQL)
		#ALTER TABLE usac.remain 
		#	DROP COLUMN IF EXISTS unacc_hc ; 
		#COMMIT; 
		#ALTER TABLE usac.remain 
		#	ADD COLUMN unacc_hc money ; COMMIT;
		updCur.execute(updSQL)

#update the unaccouted for in high cost
def retUnAcc(aST):
	myList = []
	mySQL = "SELECT state, " 
	mySQL = mySQL + "SUM(hcl+hcm+ias+icls+lss+sna+svs) as high_cost, "
	mySQL = mySQL + "SUM(fhcs+incs+icc+mobility_1+cacm+rbe+acam+bls+ak_plan+caf2_auc+pr_mobile+usvi_mobile+acam_2) as caf,"
	mySQL = mySQL + "COUNT(distinct sac) "
	mySQL = mySQL + "FROM " + sch + "." + disTB + " "
	mySQL = mySQL + "WHERE year in ('2015', '2016', '2017', '2018', '2019', '2020') "
	mySQL = mySQL + "AND sac not in ( "
	mySQL = mySQL + "SELECT DISTINCT sac "
	mySQL = mySQL + "FROM " + sch + "." + sacTB + " "
	mySQL = mySQL + ") "
	mySQL = mySQL + "AND state = '" + aST + "' "
	mySQL = mySQL + "GROUP BY state "
	mySQL = mySQL + "ORDER BY state "
	mySQL = mySQL + "; "
	# print (mySQL)
	# SELECT state, 
	#		SUM(hcl+hcm+ias+icls+lss+sna+svs) as high_cost, 
	#		SUM(fhcs+incs+icc+mobility_1+cacm+rbe+acam+bls+ak_plan+caf2_auc+pr_mobile+usvi_mobile+acam_2) as caf,
	#		COUNT(distinct sac) 
	#	FROM usac.disbursement 
	#	WHERE year in ('2015', '2016', '2017', '2018', '2019', '2020') 
	#	AND sac not in 
	#	( 
	#		SELECT DISTINCT sac 
	#		FROM usac.sac 
	#	) 
	#	AND state = 'MS' 
	#	GROUP BY state 
	#	ORDER BY state ; 


	aCur.execute(mySQL)
	for row	in aCur:
		myList.append(row[1]) #unaccounted for High Cost
		myList.append(row[2]) #un accounted for CAF
		myList.append(row[3]) #number of SACs

	# print(myList)
	return(myList)

#now update the exisint polygon with the difference
def updateTB(aST, Vals):
	#update High Cost
	updSQL = "UPDATE " + sch + "." + outTB + " "
	updSQL = updSQL + "SET unacc_hc= '" + Vals[0] + "' "
	updSQL = updSQL + "WHERE state_abbv = '" + aST + "' "
	updSQL = updSQL + "; COMMIT; "
	# print (updSQL)
	# UPDATE usac.remain SET unacc_hc= '$0.00' ; COMMIT; 
	# COMMIT;
	updCur.execute(updSQL)

	#update CAF
	updSQL = "UPDATE " + sch + "." + outTB + " "
	updSQL = updSQL + "SET unacc_caf= '" + Vals[1] + "' "
	updSQL = updSQL + "WHERE state_abbv = '" + aST + "' "
	updSQL = updSQL + "; COMMIT; "
	# print (updSQL)
	# UPDATE usac.remain SET unacc_caf= '$460,332,117.21' ; COMMIT; 
	# COMMIT;
	updCur.execute(updSQL)

	#update total
	updSQL = "UPDATE " + sch + "." + outTB + " "
	updSQL = updSQL + "SET total = unacc_hc+unacc_caf "
	updSQL = updSQL + "WHERE state_abbv = '" + aST + "' "
	updSQL = updSQL + "; COMMIT; "
	# print (updSQL)
	# UPDATE usac.remain SET total = unacc_hc+unacc_caf 
	#	WHERE state_abbv = 'MS' ; 
	#COMMIT; 
	updCur.execute(updSQL)

	#update num_sac
	updSQL = "UPDATE " + sch + "." + outTB + " "
	updSQL = updSQL + "SET num_sac= " + str(Vals[2]) + " "
	updSQL = updSQL + "WHERE state_abbv = '" + aST + "' "
	updSQL = updSQL + "; COMMIT; "
	# print (updSQL)
	# UPDATE usac.remain 
	#	SET unacc_caf= '$460,332,117.21' ; 
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

initFields()


# #for the coop_boundaries data
for myST in myList:
	print "	starting: " + myST[0]
	myVals = retUnAcc(myST[0])
	if len(myVals) > 0:
		updateTB(myST[0], myVals)
#clean up
aCur.close()
insCur.close()
updCur.close()
mkCur.close()
