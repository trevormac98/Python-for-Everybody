'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by houred smallest to largest
'''

fname = input('Enter File name: ')
fh = open(fname)
counts = dict()
for line in fh:
	line = line.rstrip()
	if line == "": 
		continue
	words = line.split()
	if words[0] != "From" :
		continue
	freq = words[5].split(":")
	counts[freq[0]] = counts.get(freq[0], 0) + 1


lst = list()
for key, val in counts.items():
	lst.append(key, val)

lst.sort()

for time, count in lst:
	print(time, count)

	