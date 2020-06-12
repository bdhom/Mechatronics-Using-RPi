#Brycen Dhom
#ECE 492-501
#6/9/2020

import RPi.GPIO as GPIO
import time

led_pins = [4,17,18,27]
led_pins_rev = [27,18,17,4]
GPIO.setmode(GPIO.BCM)

for pin in led_pins:
	GPIO.setup(pin,GPIO.OUT)

down = True
up = False

try:
	while True:
		while down:
			for i,pin in enumerate(led_pins):
				GPIO.output(pin,1)
				time.sleep(0.1)
				if i == 3:
					down = False
					up = True
					break
				GPIO.output(pin,0)
				time.sleep(0.1)
		while up:
			for i,pin in enumerate(led_pins_rev):
				GPIO.output(pin,1)
				time.sleep(0.1)
				if i == 3:
					down = True
					up = False
					break
				GPIO.output(pin,0)
				time.sleep(0.1)
except KeyboardInterrupt:	
	print('Cleaning Up')
	GPIO.cleanup()
