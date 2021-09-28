#! /usr/bin/python

# Continuosly monitor momentary button
# when pressed, get current date 
# and create a new photo image, name it 
# {timestamp}.jpg and save it in /home/pi

import os
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

HM = '/home/pi/Pictures'
MEDIA = '/media/pi'

media_dirs = os.listdir(MEDIA)
if( len ( media_dirs ) ) > 0 and os.access( MEDIA + '/' + media_dirs[0],
        os.W_OK ):
    OUT = MEDIA
else:
    OUT = HM

camera = PiCamera()
shutter_button = Button(20)

def capture():
    timestamp = datetime.now().isoformat()
    camera.capture( OUT + '/%s.jpg' % timestamp )



shutter_button.when_pressed = capture

pause()


