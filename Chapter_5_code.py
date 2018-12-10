''' Write a program that repeatedly prompts a user for integer numbers until the user enters done. Once done is entered, print out the largest and smalled
of the numbers. If the user enters anything other than a valid number, catch it with a try/except and put out an appropriate message and ignore
the number. Enter 7, 2, bob, 10 and 4 and math the output. '''

largest = None
smallest = None

while True: 
	sval = input('Enter a number: ')
	
	if sval == 'done' :
		break
	try:
		fval = float(sval)
	except:
		print('Invalid input')
		continue	
    
    for number in range(sval):
		if largest is None or largest < sval:
            largest = sval
                
        elif smallest is None or smallest > sval:
            smallest = sval    
	
print ('Maximum is ', largest)
print ('Minimum is ', smallest)

