# Input: CSV file -------> time,userID,action  (the information about the object on which action is performed i.e. "slip" and "note" is totall lost)
# Output: the sequential order of actions performed by each team. That is to say that the information for "each actor" and "time information" is totally lost. 


import glob, csv, os
import pickle
import re


def removeSuccessiveDuplicates(theString):
	for i in theString:
		dup = i+i
		theString = re.sub(dup, i, theString)
	return theString


def csvToActionDB(dbFileName, dirName):
	listOfFiles = glob.glob(os.getcwd()+"/"+ dirName +"/*.csv")
	# pickle.dump(list(listOfFiles), "listOfFiles.txt")
	print listOfFiles, len(listOfFiles), type(listOfFiles)
	fWrite = open(dbFileName, 'w+')
	writer = csv.writer(fWrite)
	fWrite1 = open(dbFileName[:-3]+"rduplDB", 'w+')
	writer1 = csv.writer(fWrite1)
	fWrite2 = open(dbFileName[:-3]+"stringDB", 'w+')
	writer2 = csv.writer(fWrite2)
	with open(dbFileName[:-3]+"pickle",'wb') as f:
		pickle.dump(listOfFiles,f)

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
		# print eachList
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
		writer2.writerow(eachTransaction)
		setOfAbbrTransactions.append(eachTransaction)
		# print eachTransaction, type(eachTransaction)
		writer.writerow(",".join(map(str,eachTransaction))) # creating comma seperated sequences, successive duplicates are present
		eachTransaction = removeSuccessiveDuplicates(eachTransaction[0]) # remove successive duplicates
		writer1.writerow(",".join(map(str,[eachTransaction]))) # create CSV after removing successive duplicates
	
	
	# print setOfAbbrTransactions




# This function creates two seperate databases, each for 'High Achievers' and 'Low Achievers'
# The name of the output files of createDB() function have .stringDB as their suffixes. 

def createDB():
	names = ["HighAchievers", "LowAchieverse"]
	for dirName in names:
		fn = os.getcwd()+"/"+ dirName +"/tran" + dirName[:-9] + ".csv"
		os.remove(fn) if os.path.exists(fn) else None
		os.remove(fn[:-3]+"stringDB") if os.path.exists(fn[:-3]+"stringDB") else None
		csvToActionDB(fn, dirName)

		

# Run this function
createDB()



