import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led_pin = 11
CLK = 23
DOUT = 13
DIN = 15
CS = 19

GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)

pwm_led = GPIO.PWM(led_pin,500)
pwm_led.start(100)

pot = 0

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
		value = readadc(pot, CLK, DOUT, DIN, CS)
		duty_raw = value/1023.0
		print("Brightness: {:7.2%}".format(duty_raw))
		duty = int(duty_raw * 100.0)
		pwm_led.ChangeDutyCycle(duty)
		#print(duty)
		time.sleep(1)
except KeyboardInterrupt:
	print("Cleaning up")
	GPIO.cleanup()
