# This file reads name.stringDB file as input. That is a file which has the information about sequential ordering of actions 
# i.e. a file which ignores authorship infomation and contains successive duplicates.
# 



from scipy.stats import itemfreq
import numpy as np
import glob
import os


def count_unique(keys):
    uniq_keys = np.unique(keys)
    bins = uniq_keys.searchsorted(keys)
    return uniq_keys, np.bincount(bins)


# with open('/home/teste/workspace/newcastlemarch20/workData/LowAchieverse/tranLowA.stringDB') as f:

#     content = f.readlines()
#     allGrams = []
#     top_nGrams = []
#     topNgrams_count = []
#     for N in range(4,11):
# 	    for s in content:
# 	    	grams = [s[i:i+N] for i in xrange(len(s)-N)]
# 	    	allGrams.extend(grams)
# 	    	the_ngrams, ngrams_count  = count_unique(grams)
# 	    	sortedKeys = np.argsort(ngrams_count)
# 	    	top_15 = sortedKeys[-15:]
# 	    top_nGrams = top_nGrams + list(the_ngrams[top_15])
# 	    topNgrams_count = topNgrams_count + list(ngrams_count[top_15])



def nGramGenerator(inputFile, outFile, numberOfTopGrams = 15, minN = 4, maxN = 10):
	with open(inputFile[0]) as f:
		  content = f.readlines() # The entite file is read into a list. Each element of the list is a string of actions, which ends with a new line character.
		  allGrams = []  # gives all the N-grams in list. Each element of list is a string of n-gram. 
		  top_nGrams = []
		  topNgrams_count = []
		  for N in range(minN, maxN + 1):
		  	for s in content:
		  		grams = [s[i:i+N] for i in xrange(len(s)-N)]
		  		allGrams.extend(grams)
		  		the_ngrams, ngrams_count  = count_unique(grams)  # This reads the list of all n-grams and finds out how their respective count. 
		  		sortedKeys = np.argsort(ngrams_count)  # sorts the index of n-gram list from low apperance to high appearance.
		  		top_count = sortedKeys[-numberOfTopGrams:]  # highest occuring n-grams are taken into account.
		  	top_nGrams = top_nGrams + list(the_ngrams[top_count]) # Top "numberOfTopGrams" are put in the list. 
		  	topNgrams_count = topNgrams_count + list(ngrams_count[top_count]) # The frequency of "numberOfTopGrams" is also put in the list in increasing order for each N.

	top_nGrams = list(top_nGrams)
	top_nGrams_CSV = [','.join(list(s)) for s in top_nGrams]
	fWrite = open(outFile, 'w+')
	fWrite2 = open(outFile[:-6]+"_csv.nGram", 'w+')
	for line in top_nGrams:
		# print line
		fWrite.write(line)
		fWrite.write('\n')
	for line in top_nGrams_CSV:
		# print line
		fWrite2.write(line)
		fWrite2.write('\n')



def createDBTopNgrams():
	names = ["HighAchievers", "LowAchieverse"]
	for dirName in names:
		fIn = glob.glob(os.getcwd()+"/"+ dirName +"/*.stringDB")
		fOp = os.getcwd()+"/"+ dirName +"/nGram" + dirName[:-9] + ".nGram"
		os.remove(fOp) if os.path.exists(fOp) else None
		nGramGenerator(fIn, fOp, 15, 4, 10) 

createDBTopNgrams()



# for line in top_nGrams:
# 	print list(line)





