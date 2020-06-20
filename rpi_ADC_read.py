#Brycen Dhom
#ECE 492 - 501
#6/19/20

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

CLK = 11
DOUT = 13
DIN = 15
CS = 19

GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)

pot = [0,1]

def readadc(num, clk, dout, din, cs):
	if ((num > 7) or (num < 0)):
		return -1
		
	GPIO.output(cs, 1)
	GPIO.output(clk, 0)
	GPIO.output(cs, 0)
	
	command = num
	command	|= 0x18
	command <<= 3
	
	for i in range(5):
		if (command & 0x80):
			GPIO.output(din, 1)
		else:
			GPIO.output(din, 0)
			
		command <<=1
		GPIO.output(clk, 1)
		GPIO.output(clk, 0)
		
	out = 0
		
	for i in range(12):
		GPIO.output(clk,1)
		GPIO.output(clk,0)
		out <<= 1
		out |= GPIO.input(dout)
		
	GPIO.output(cs, 1)
	out >>= 1
	return out
	
try:
	while True:
		for i in range(2):
			value = readadc(pot[i], CLK, DOUT, DIN, CS)
			print("ADC %i" %i)
			print("Reading {:4} of 1023 ".format(value))
			print("({:7.2%})".format(value/1023.0))
			time.sleep(1)
except KeyboardInterrupt:
	print("Cleaning up")
	GPIO.cleanup()
