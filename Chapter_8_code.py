'''8.4: Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using
the split() method. The program should build a list of words. For each word on each line check to see if the 
word is already in the list and if not append it to the list. When the program completes, sort and print the
resulting words in alphabetical order.
'''
fname = input("Enter file name: ")
fh = open(fname)
words = []

for line in fh:
	line = line.split()

	if len(line) == 0:
		continue

	for word in line:
		if word in words:
			continue
		else:
			words.append(word)
words.sort()

print(words)






'''8.5: Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From' =, 
you will parse the From line using split() and print out the second word in the line (ie. the entire address
of the person who sent the message). Then print out a count at the end. Hint: Make sure not to include the lines
that start with 'From:'
'''

fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
	line = line.rstrip()
	if line.startswith('From:'):
		count = count + 1
		words = line.split()
		print(words[1])

print('There were', count, 'lines in the file with From as the first word')