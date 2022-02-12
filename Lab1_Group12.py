welcome_message = """
🆆🅴🅻🅲🅾🅼🅴 ❗
"""


print(welcome_message)

#Ask user to enter the number of cents
cent = int(input('How many cents ? '))

qt="quarter"
nk="nickel"
dm="dime"
py="penny"

remainder1 = cent%25
quarter= int((cent-remainder1)/25)

remainder2=remainder1%10
dime=int((remainder1-remainder2)/10)

remainder3=remainder2%5
nickel=int((remainder2-remainder3)/5)

remainder4 = remainder3
penny= remainder4


if(quarter>1):
   qt="quarters"
if(nickel>1): 
   nk="nickels"
if(dime>1): 
   dm="dimes"
if(penny>1):
   py="pennies"

lst = [
        [quarter, qt],
        [dime, dm],
        [nickel, nk],
        [penny, py]
]


and_ = None

counter = 0
for i in lst:
	if i[0] >= 1:
		counter+=1


if counter >= 2:
	and_ = True
		

 
string = f">>>{cent}\n"
if and_ == True:
	for i in lst[:-1]:
		if i[0] <= 0:
			continue
		string+=f"{i[0]} {i[1]},"
	string = string[:-1]
	string += f" and {lst[-1][0]} {lst[-1][1]}"

if and_ == None:
	for i in lst:
		if i[0] <= 0:
			continue
		if i[0] >= 1:
			print(i[0], i[1])
			string += f"{i[0]} {i[1]}"

print(string)


