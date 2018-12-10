'''Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time and a half for the hourly rate 
for all hours worked above 40 hours. Put the logic to do the computation of time and a half in function called computepay() and use the 
function to do the computation. The function should return a value. Use 45 hours and a rate of 10.5 per hour to test the program.
The pay should be 498.75. You should use input to read a string and float() to convert the string to a number. Do not worry 
about error checking the user input unless you want to. You can assume the user types numbers properly. Do not name your variable
sum or use the sum() function. '''

hrs = input("Enter hours:")
hrs = float(hrs)
rate = input("Hourly rate:")
rate = float(rate)

def computepay(hrs): 

	if hrs >40:
		print (40 * rate + (hrs - 40)*1.5*rate)

	else:
		print (hrs * rate)

computepay(hrs)

''' The way this code is right now is I can type in the hrs and rate but then it errors our on the def. I missed
something in the explanation of def and I need to go back and review that part of the video. The problem has to be somewhere
in the if/else statement and returning math.'''

'''Latest note, when I did print in the if/else statement instead of return, and ran the program, I got the desired result. 
This is also true when I put the hrs in the () of computepay. Note, I did def computepay() and def computepay(hrs)
and both work. Note, that whatever I had in the first () of computepay, I had to put in the second computepay() at bottom of 
code. Note, when wanting to show result of a def function, which in this case is computepay(), you do not need to say
print (computepay) as this will not work. The way it is now, is the correct way. '''

''' The assignment has me change print to return in the if/else statement. Then it had me do print (computepay()). Both ways work.
I did not have the (hrs), instead just () and I passed.'''