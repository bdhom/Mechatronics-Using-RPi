from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

effects = ['negative','watercolor','sketch','solarize','colorswap']

for i in range(5):
	camera.image_effect = effects[i]
	camera.annotate_text = 'Image Effect: %s' %effects[i]
	sleep(1)
	camera.capture('/home/pi/Desktop/effect%s.jpg' %i)

camera.stop_preview()

camera.close()
