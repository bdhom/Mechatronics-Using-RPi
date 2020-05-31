from matplotlib.pyplot import *
from numpy import *

t = arange(1,3,0.02)
T = 6*log(t)-7*exp(0.2*t)

figure(1)
clf()
plot(t,T)

title('Dhom-Plot')
xlabel('Time (Minutes)')
ylabel('Temperature (Degrees Celsius)')

print("Hello World! I just wrote my first Python program. Yayyyyyyyy")
print("Brycen Dhom")

show()
