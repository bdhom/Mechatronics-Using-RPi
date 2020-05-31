#Brycen Dhom
#ECE 492-001
#5/27/2020

Hours = int(input("Please enter the number of hours:"))
RPH = int(input("Please enter the rate per hour:"))
Gross = 0

if Hours > 40:
    Gross = 40 * RPH
    Gross = Gross + ((Hours - 40) * RPH * 1.5)
else:
    Gross = Hours * RPH

print('Your gross pay: $' + str(Gross))
    
