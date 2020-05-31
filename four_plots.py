#Brycen Dhom
#ECE 492-001
#5/27/2020

from matplotlib.pyplot import *
from numpy import *
from copy import *

def my_plot(T,Y,shape = '',x_label = 'Time (s)',fig_num = 1,cl_fig = True, Name = '',):
    figure(fig_num)
    
    if cl_fig:
        clf()

    if shape:
        plot(T,Y,shape)
    else:
        plot(T,Y)

    if Name:
        title(Name)
    if x_label:
        xlabel(x_label)
        
t = arange(0,1,0.01)
y = 2.0*sin(2*pi*t)
y1 = copy(y)
y2 = copy(y)
y3 = copy(y)
y4 = copy(y)

#1: Cryptic
y1[y1 < 0.5] = 0

my_plot(t,y,shape = 'r--')
my_plot(t,y1,Name = 'Cryptic',cl_fig = False)

#2: Where
inds = where(y2 < 0.5)[0]
y2[inds] = 0

my_plot(t,y,shape = 'r--',fig_num = 2)
my_plot(t,y2,Name = 'Where',fig_num = 2,cl_fig = False)

#3: For Loop
N = len(y3)
y3_new = zeros(N)

for i in range(N):
    if y3[i] > 0.5:
        y3_new[i] = y3[i]

my_plot(t,y,shape = 'r--',fig_num = 3)
my_plot(t,y3_new,Name = 'For Loop',fig_num = 3,cl_fig = False)

#4:For Loop w/ Enumerate
for i,item in enumerate(y4):
    if item < 0.5:
        y4[i] = 0

my_plot(t,y,shape = 'r--',fig_num = 4)
my_plot(t,y4,Name = 'For Loop With Enumerate',fig_num = 4,cl_fig = False)

show()
