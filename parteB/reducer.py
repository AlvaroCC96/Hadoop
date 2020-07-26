#!/usr/bin/python

import sys

total = 0
totalMounths =0
oldKey = None


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	# Get Data	
	thisKey,thisValue = data_mapped

	# Count total petitions
	totalMounths +=int(thisValue)
	
	# For new key
	if oldKey and oldKey != thisKey:
		print oldKey, "\t", total 
		oldKey = thisKey;
		total = 0

	oldKey = thisKey
	total += int(thisValue)

if oldKey != None:
	print oldKey, "\t", total

print "Total petitions:", "\t",totalMounths
