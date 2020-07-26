#!/usr/bin/python

# Patricio Araya
# Alvaro Castillo
import sys

for line in sys.stdin:
	typeRequest = ''
	code = ''
	# Get line from system data
	data = line.strip().split()
	
	# Defensive programming
	if len(data) == 10:

		# Request field formatting
		typeRequest = data[5].replace('"','')

		# Requesty type review		
		if typeRequest == "GET":
			code= data[8]			

			# Verification request code
			if code[0] == "4":
		
				# Print value
				print "{0}\t{1}".format(code,1)
