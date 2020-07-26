#!/usr/bin/python

# Patricio Araya
# Alvaro Castillo
import sys

for line in sys.stdin:
	
	# Get line from system data
	data = line.strip().split()
	
	# Defensive programming
	if len(data) == 10:

		# Request field formatting
		dateList = data[3].split(":")
		dateLog = dateList[0].split("/")
		mounth = dateLog[1]
		
		# Print key and value
		print "{0}\t{1}".format(mounth, 1)
		

		
