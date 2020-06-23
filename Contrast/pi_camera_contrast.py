from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

for i in range(5):
	con = i * 25
	camera.contrast = con
	camera.annotate_text = 'Contrast: %s' %con
	sleep(1)
	camera.capture('/home/pi/Desktop/contrast%s.jpg' %i)

camera.stop_preview()

camera.close()
