#Brycen Dhom
#ECE 492-501
#6/11/2020

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		GPIO.output(12, True)
		time.sleep(0.00001)
		GPIO.output(12, False)

		startTime = time.time()
		stopTime = time.time()

		while 0 == GPIO.input(11):
			startTime = time.time()
		while 1 == GPIO.input(11):
			stopTime = time.time()
			
		TimeElapsed = stopTime - startTime
		distance = (TimeElapsed * 34300) / 2

		print ("%.1f cm" % distance)
		time.sleep(1)
except KeyboardInterrupt:
	print('Cleaning Up')
	GPIO.cleanup()
