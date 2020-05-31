import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pins = [17,27,22]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

while True:
    number = int(input('Number 1 to 3:'))
    if number == 1:
        GPIO.output(pins[0],1)
        GPIO.output(pins[1],0)
        GPIO.output(pins[2],0)
    if number == 2:
        GPIO.output(pins[0],1)
        GPIO.output(pins[1],1)
        GPIO.output(pins[2],0)
    if number == 3:
        GPIO.output(pins[0],1)
        GPIO.output(pins[1],1)
        GPIO.output(pins[2],1)
    else:
        print('Invalid Number. Try Again!')
        GPIO.output(pins[0],0)
        GPIO.output(pins[1],0)
        GPIO.output(pins[2],0)
