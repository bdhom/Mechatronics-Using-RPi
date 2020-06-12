#Brycen Dhom
#ECE 492-501
#6/11/2020

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

c = 0

try:
	while True:
		if GPIO.input(16) == 1:
			c = (c + 1) % 8
			GPIO.output(11, (c >> 0) & 1)
			GPIO.output(13, (c >> 1) & 1)
			GPIO.output(15, (c >> 2) & 1)
			while GPIO.input(16) == 1:
				time.sleep(0.1)
except KeyboardInterrupt:
	print('Cleaning Up')
	GPIO.cleanup()
