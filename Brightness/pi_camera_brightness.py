from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

for i in range(5):
	light = i * 25
	camera.brightness = light
	camera.annotate_text = 'Brightness: %s' %light
	sleep(1)
	camera.capture('/home/pi/Desktop/brightness%s.jpg' %i)

camera.stop_preview()

camera.close()
