#Brycen Dhom
#ECE 492-001
#5/27/2020

def computepay(hours,rate):
    total_hours = hours
    pay = total_hours * rate
    
    if hours > 40:
        total_hours = total_hours + ((total_hours - 40) * 0.5)
        pay = total_hours * rate
    return total_hours, pay

Hours = int(input("Please enter the number of hours:"))
RPH = int(input("Please enter the rate per hour:"))

[Total_Time, Gross] = computepay(Hours,RPH)

print('Time with time-and-a-half: ' + str(Total_Time) + ' hours')
print('Gross pay: $' + str(Gross))
