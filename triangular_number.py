#Brycen Dhom
#ECE 492-501
#5/28/2020

number = int(input('Triangular of:'))
total = 0
check = (number * (number + 1)) / 2

for i in range(number):
    total = total + (number - i)

print('Triangular of ' + str(number) + ': ' + str(total))
print('Check: ' + str(check))
