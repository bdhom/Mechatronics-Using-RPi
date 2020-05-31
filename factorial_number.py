#Brycen Dhom
#ECE 492-501
#5/28/2020

number = int(input('Factorial of:'))
total = 1

for i in range(number):
    total = total * (number - i)

print(str(number) + '! = ' + str(total))
