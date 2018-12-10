'''In this assignment, you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute
the sum of the numbers. The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular
expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers '''
#File name: ch_11_actual.txt

import re

fname = open('ch_11_actual.txt')
extract = []
summ = 0
for line in fname:
	line = line.rstrip()
	x = re.findall('[0-9]+', line)
	extract = x + extract
for y in extract:
	summ = summ + int(y)
print ("The sum is", summ)