''' 7.1: Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.'''

fname = input("Enter file name: ")
fh = open(fname)
fl = fh.read()
newfl = fl.upper()
newflow = newfl.rstrip()
print(newflow)
#had to add rstrip() to get it to work on grading server. Other way worked as well (no line 8 and print was print(newfl))


'''7.2: Write a program that prompts a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8745
Count these lines and extract the floating point values from each of the lines and compute the average of those values
and produce an output as shown below. do not use the sum() function or a variable named sum in your solution.
File name is mbox-short.txt
'''
fname = input("Enter text file:, ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    first = line.find(':')
    number = float(line[first+1:])
    total=total+number
    count = count+1    
print ("Average spam confidence:", total/count)

