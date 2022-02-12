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

print (remainder3)

if(quarter>1):
   qt="quarters"
if(nickel>1): 
   nk="nickels"
if(dime>1): 
   dm="dimes"
if(penny>1):
   py="pennies"
   
#print the output  
print(quarter,qt,",",dime,dm,",",nickel,nk,"and",penny,py)

