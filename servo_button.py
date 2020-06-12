#Brycen Dhom
#ECE 492-501
#6/11/2020

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(12,50)
p.start(7.5)

try:
	while True:
		if (GPIO.input(11) == 1) and (GPIO.input(13) == 1):
			p.ChangeDutyCycle(7.5)
		if (GPIO.input(11) == 1) and (GPIO.input(13) != 1):
			p.ChangeDutyCycle(2.5)
		if (GPIO.input(11) != 1) and (GPIO.input(13) == 1):
			p.ChangeDutyCycle(12.5)
except KeyboardInterrupt:
	print('Cleaning Up')
	p.stop()
	GPIO.cleanup()
