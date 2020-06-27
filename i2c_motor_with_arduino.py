import smbus
import time
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)
address = 0x04
state = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 100)

pwm.start(0)

GPIO.output(31, True)
GPIO.output(33, False)

def writeNumber(value):
	bus.write_byte(address, value)
	return -1
	
def readNumber():
	number = bus.read_byte(address)
	return number
	
try:
	while True:
		writeNumber(0)
		time.sleep(1)
		number = readNumber()
		
		if (number == 1):
			if (number != state):
				print("Sytem Enabled")
				state = 1
		elif (number == 0):
			if (number != state):
				print("System Disabled")
				state = 0
				pwm.ChangeDutyCycle(0)
				
		if (state == 1):
			writeNumber(1)
			print("Motor Speed:")
			time.sleep(1)
			number = readNumber()
			percent = number / 2.56
			print(percent)
			pwm.ChangeDutyCycle(percent)
			
			
except KeyboardInterrupt:
	print("Cleaning up")
	pwm.stop()
	GPIO.cleanup()
