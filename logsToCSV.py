# Written by Raghvendra Jain on Dec 24, 2015
# We take raw log input i.e. all the 10 files and produce the CSV as output.
# This file reads all the log files and takes the time, userId and Action of the event.
# Some userId were negavtive I just took their absolute value and made the format of following:
# the logsToCSV() function extracts the timed sequence of the all 'Action' parameters irrespective of their 'Author'.
# The CSV contains information about Time, author and Action"""
# Input:  RAW log file ---> time,userID,action,objName
# Output: CSV file -------> time,userID,action

import glob, csv, os

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
