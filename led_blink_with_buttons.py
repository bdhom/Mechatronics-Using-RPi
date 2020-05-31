import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pins = [17,27,22]
buttons = [5,6,13,12]
conditions = [False,False,False,False]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

for button in buttons:
    GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        conditions[0] = GPIO.input(buttons[0]) == 1
        conditions[1] = GPIO.input(buttons[1]) == 1
        conditions[2] = GPIO.input(buttons[2]) == 1
        conditions[3] = GPIO.input(buttons[3]) == 1
        if conditions[0]:
            GPIO.output(pins[0],1)
            GPIO.output(pins[1],0)
            GPIO.output(pins[2],0)
        elif conditions[1]:
            GPIO.output(pins[0],1)
            GPIO.output(pins[1],1)
            GPIO.output(pins[2],0)
        elif conditions[2]:
            GPIO.output(pins[0],1)
            GPIO.output(pins[1],1)
            GPIO.output(pins[2],1)
        elif conditions[3]:
            GPIO.output(pins[0],0)
            GPIO.output(pins[1],0)
            GPIO.output(pins[2],0)
            
except KeyboardInterrupt:
    GPIO.cleanup()
