#load_highcost.py
#load the high cost data into a table
#mike byrne
#august 30, 2021

#variables and importing
import psycopg2
import psycopg2.extras
import time
import os
import csv


now = time.localtime(time.time())
print "start time:", time.asctime(now)
print "	begin: " + (__file__)

#
#******************************************************
#						VARIABLES
#******************************************************
#

# Establish Database Configuration Properties
DATABASE_HOST = os.getenv('DATABASE_HOST', '127.0.0.1')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'postgres')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = "fcc"

myConn = "dbname=" + DATABASE_NAME + " " + \
	"host=" + DATABASE_HOST + " " + \
	"port=" + DATABASE_PORT + " " + \
	"user=" + DATABASE_USERNAME + " " \
	"password=" + DATABASE_PASSWORD

sch = "usac"

inDir = "/Users/mike/Documents/Data/USAC/disbursement/source_data/2021_08/"
inFile = "High_Cost_Disbursements.csv"

dataDict = []
#
#******************************************************
#						FUNCTIONS 
#******************************************************
#	
#create the output table
def initOutput(aTab):
	# fcc_form_498_ID,sac,study_area_name,state,year,month,fund_type,amount_disbursed
	mySQL = "DROP TABLE IF EXISTS " + sch + "." + aTab 
	mySQL = mySQL + " ; COMMIT; "
	aCur.execute(mySQL)
	mySQL = "CREATE TABLE " + sch + "." + aTab + " ("
	mySQL = mySQL + "fcc_form_498_id character varying, "
	mySQL = mySQL + "sac character varying(6), "
	mySQL = mySQL + "study_area_name character varying, "
	mySQL = mySQL + "state_abbv character varying(2), "
	mySQL = mySQL + "year_disbursed integer, "
	mySQL = mySQL + "month_disbursed character varying(3), "
	mySQL = mySQL + "fund_type character varying(20), "
	mySQL = mySQL + "amount_disbursed numeric(10,2) "
	mySQL = mySQL + ") WITH (OIDS = FALSE) ;"

	# print (mySQL)
	# CREATE TABLE usac.disburse_test 
	# 	(
	# 	fcc_form_498_id character varying, 
	# 	sac character varying(6), 
	# 	study_area_name character varying, 
	# 	state_abbv character varying(2), 
	# 	year_disbursed integer, 
	# 	month_disbursed character varying(3), 
	# 	fund_type character varying(10),
	# 	amount_disbursed numeric(10,2) 
	# 	) 
	# 	WITH (OIDS = FALSE) ;
	aCur.execute(mySQL)

#add a comment for the shape
def addComment(aTab):
	myComment = aTab + ": "
	myComment = myComment + "Table added on: " + str(time.asctime(now)) + ". "
	myComment = myComment + "Data source directory is: " + inDir + ". "
	myComment = myComment + "Data source file is: " + inFile + ". "

	mySQL = "COMMENT ON TABLE " + sch + "." + aTab + " "
	mySQL = mySQL + "IS '" + myComment + "'; "
	mySQL = mySQL + "COMMIT; "
	# print (mySQL)
	# COMMENT ON TABLE usac.disburse_test IS 
	# 	'disburse_test: Table added on: Mon Aug 30 12:37:15 2021. Data source directory is: /Users/mike/Documents/Data/USAC/disbursement/source_data/2021_08/. Data source file is: test.csv. '; 
	# 	COMMIT; 
	aCur.execute(mySQL)


#perform the vaccum
def myVacuum(aTab):
	vConn = psycopg2.connect(myConn)
	# #aCur
	theCur = vConn.cursor()
	old_isolation_level = vConn.isolation_level
	vConn.set_isolation_level(0)
	print "			vaccuming: " + sch + "." + aTab	
	mySQL = "VACUUM ANALYZE " + sch + "." + aTab + "; "
	theCur.execute(mySQL)
	vConn.set_isolation_level(old_isolation_level)
	# #clean up
	theCur.close()


def loadData():
	myFile = inDir + inFile
	with open (myFile) as dataFile:
		reader = csv.DictReader(dataFile)
		for row in reader:
			# print (row["fcc_form_498_ID"])
			aID = row["fcc_form_498_ID"]
			aSac = row["sac"]
			aName = row["study_area_name"]
			aST = row["state"]
			aYear = row["year"]
			aMonth = row["month"]
			aFund = row["fund_type"]
			aAmt = row["amount_disbursed"]

			dataDict.append([
				aID,aSac,aName,aST,aYear,aMonth,aFund,aAmt
				])
	return()

#batch insert
def batchIns(aTab):
	insSQL = "INSERT INTO " + sch + "." + aTab + ""
	insSQL = insSQL + "("
	insSQL = insSQL + "fcc_form_498_id,sac,"
	insSQL = insSQL + "study_area_name,state_abbv,"
	insSQL = insSQL + "year_disbursed,month_disbursed,"
	insSQL = insSQL + "fund_type,amount_disbursed"
	insSQL = insSQL + ")"
	insSQL = insSQL + " VALUES "
	insSQL = insSQL + "("
	insSQL = insSQL + "%s,%s," 
	insSQL = insSQL + "%s,%s," 
	insSQL = insSQL + "%s,%s," 
	insSQL = insSQL + "%s,%s" 
	insSQL = insSQL + ") "
	insSQL = insSQL + "; "
	insSQL = insSQL + "COMMIT; "

	# print (insSQL)
 	psycopg2.extras.execute_batch(aCur, insSQL, dataDict)

#
#******************************************************
#						MAIN 
#******************************************************
#	
conn = psycopg2.connect(myConn)
#make cursor - used to make a new table
aCur = conn.cursor()

myTab = "disbursed"
initOutput(myTab)
addComment(myTab)
loadData()
# print (dataDict)
batchIns(myTab)
myVacuum(myTab)

#clean up
aCur.close()

#end
print "		finished: " + (__file__)
now = time.localtime(time.time())
print "end time:", time.asctime(now)
