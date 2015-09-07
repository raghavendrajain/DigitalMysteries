# This file reads all the log files and takes the time, userId and Action of the event.
# Some userId were negavtive I just took their absolute value and made the format of following:

import glob, csv

def start():
	""" This function creates the list of all log files"""
	listOfFiles = glob.glob('*.log')
	return listOfFiles


def logsToCSV():
	""" This function takes all the log files as input and extracts the timed sequence of the all 'Action' parameters irrespective of their 'Author'.
	The CSV contains information about Time, author and Action"""
	listOfFiles = start()
	for eachFile in listOfFiles:
		f = open(eachFile, 'rU')
		fWrite = open(eachFile[:-3] + "csv", 'w')
		csv_f = csv.reader(f)
		rowCount = 0
		for row in csv_f:
			rowCount = rowCount + 1
			if(len(row)) > 3 and rowCount > 1:
				rowL = [row[0], abs(int(row[1])), row[2]]
				writer = csv.writer(fWrite)
				writer.writerow(rowL)
				print rowL, rowCount


def csvToActionDB(dbFileName):
	logsToCSV()
	listOfFiles = glob.glob('*.csv')
	# print listOfFiles, len(listOfFiles)
	fWrite = open(dbFileName, 'w+')
	writer = csv.writer(fWrite)
	setOfTransactions = []
	for eachFile in listOfFiles:
		eachTransaction = []
		f = open(eachFile, 'rU')
		csv_f = csv.reader(f)
		for row in csv_f:
			eachTransaction.append(row[2])
		setOfTransactions.append(eachTransaction)
	C1 = ['MOVE','ENLARGE', 'NORMAL', 'SHRINK', 'ROTATE', 'ADD_OBJ_TO_GROUP', 'UPDATE_RELATION', 'REMOVE_OBJ_FROM_GROUP' ]
	setOfReducedTransactions = []
	for eachList in setOfTransactions:
		eachTransaction =[]
		for item in eachList:
			if item in C1:
				eachTransaction.append(item)
		setOfReducedTransactions.append(eachTransaction)
	print len(setOfReducedTransactions)
	global setOfAbbrTransactions
	setOfAbbrTransactions = []
	for eachList in setOfReducedTransactions:
		print eachList
		eachTransaction = []
		for index, value in enumerate(eachList):
			if value == "MOVE":
				eachList[index] = "M"
			if value == "ROTATE":
				eachList[index] = "R"
			if value == "ENLARGE":
				eachList[index] = "E"
			if value == "NORMAL":
				eachList[index] = "N"
			if value == "SHRINK":
				eachList[index] = "S"
			if value == "UPDATE_RELATION":
				eachList[index] = "U"
			if value == "REMOVE_OBJ_FROM_GROUP":
				eachList[index] = "R"
			if value == "ADD_OBJ_TO_GROUP":
				eachList[index] = "G"
		eachTransaction.append(''.join(eachList))
		writer.writerow(eachTransaction)
		setOfAbbrTransactions.append(eachTransaction)
	print setOfAbbrTransactions

csvToActionDB('tran.DB')