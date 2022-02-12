# CIS-117 Lab1

# Group 12#

# Jacob Hanna, Sebastian Campos

# Description of program
"""
This program:
	prints a welcome message
	takes input of amount of cents
	print the amount of cents using the fewest number of coins
"""


#Welcome message
welcome_message = """
🆆🅴🅻🅲🅾🅼🅴 ❗
"""

#print welcome message to user
print(welcome_message)

#Ask user to enter the number of cents
cent = int(input('How many cents ? '))

#define names of cents
qt="quarter"
nk="nickel"
dm="dime"
py="penny"


#get number of quarters
remainder1 = cent%25
quarter= int((cent-remainder1)/25)

#get number of dimes
remainder2=remainder1%10
dime=int((remainder1-remainder2)/10)

#get number of nickels
remainder3=remainder2%5
nickel=int((remainder2-remainder3)/5)

#get number of pennies
remainder4 = remainder3
penny= remainder4


# contitionals to check if defined names should be
# singular or plural
if(quarter>1):
   qt="quarters"
if(nickel>1): 
   nk="nickels"
if(dime>1): 
   dm="dimes"
if(penny>1):
   py="pennies"


# build a list of variables to iterate over
lst = [
        [quarter, qt],
        [dime, dm],
        [nickel, nk],
        [penny, py]
]


#conditional to check if `and` must be added to final output
and_ = False


#iterate over list adding to counter anytime 
#a cent count is above or equal to 1
counter = 0
for i in lst:
	if i[0] >= 1:
		counter+=1

#if more than one cent count is greater than one
#set and_ to True
if counter >= 2:
	and_ = True
		
#begin building the final string with our `cent` value at the begining
string = f">>>{cent}\n"

#if `and` is true build a string with `and` before the last value 
if and_ == True:
	#iterate over count, names list
	for i in lst:
		#if count is less than or equal to 0, skip to next iteration
		if i[0] <= 0:
			continue
		#else, add count and name to string
		string+=f"{i[0]} {i[1]},"
	#remove last comma in string
	string = string[:-1]
	#split string by  last comma
	string =string.split(",", -1)
	#join all element up to the last element from the string split list
	#by a comma. then add ` and ` plus the final string split list element
	string = ",".join(string[:-1]) + " and " + string[-1]

#if `and` is false build string with one value 
if and_ == False:
	for i in lst:
		if i[0] <= 0:
			continue
		if i[0] >= 1:
			string += f"{i[0]} {i[1]}"

#output final message
print(string)


