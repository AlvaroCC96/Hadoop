#!/usr/bin/python

# Patricio Araya
# Alvaro Castillo

import sys

total = 0
totalKeys =0
oldKey = None


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue
	
	thisKey,thisValue = data_mapped
	
	# Total keys 
	totalKeys +=int(thisValue)
	if oldKey and oldKey != thisKey:
		# Print code and total 
		print oldKey, "\t", total 
		oldKey = thisKey;
		total = 0

	oldKey = thisKey
	total += int(thisValue)

if oldKey != None:
	print oldKey, "\t", total

print "Total 4XX errors:", "\t",totalKeys
