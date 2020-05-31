#Brycen Dhom
#ECE 492-501
#5/28/2020

from numpy import *

x = zeros(3)

x[0] = input('What is x?:')
x[1] = input('What is y?:')
x[2] = input('What is z?:')

x_odd = x % 2
odd = any(x_odd == 1)

if odd:
    x_new = x * x_odd
    print('Largest odd: ' + str(max(x_new)))
else:
    print('There is not a large odd number!')
