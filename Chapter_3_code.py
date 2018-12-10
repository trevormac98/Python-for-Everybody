#Assignment 3.1: Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 time the hourly rate for all hours worked over 40.

hrs = input("Enter hours:")
hrs = float(hrs)
rate = input("Hourly rate:")
rate = float(rate)

if hrs <= 40:
	pay = hrs * rate
elif hrs> 40:
	pay = 40 * rate + (hrs - 40)*1.5*rate
else:
	print(Wrong)

print(pay)


#Assignment 2. Add a Try/Except statement to protect against the user typing the hours or hourly rate in letters instead of as numbers.

hrs = input("Enter hours:")
rate = input("Enter hourly rate:")

try:
	hrs = float(hrs)
	rate = float(rate)
except:
	print("Error, please enter numeric input")
	quit()
	#quit line above is to not show anything other errors since code wont work if non numeric value is entereted

print(hrs, rate)
if hrs <= 40:
	pay = hrs * rate
elif hrs> 40:
	pay = 40 * rate + (hrs - 40)*1.5*rate
else:
	print(Wrong)

print(pay)

#Assignment 3. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
#If the score is between 0.0 and 1.0, print a grade using the following table: 
''' >=0.9 A
	>=0.8 B
	>=0.7 C
	>=0.6 D
	< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 
0.85 '''
score = input("Enter Score: ")
try:
	score = float(score)
except:
	print("Please enter a score between 0.0 and 1.0")
	quit()

if score >= 0.9:
	print("A")
elif score >= 0.8:
	print("B")
elif score >= 0.7:
	print("C")
elif score >= 0.6:
	print("D")
else:
	print("F")
