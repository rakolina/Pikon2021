#! /usr/bin/python

# Continuosly read from the momentary button
# when pressed, get current date 
# and create a new photo image, name it 
# {timestamp}.jpg and save it in /home/pi
# or on a removable USB drive if available

import os
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

HM = '/home/pi/Pictures/'
MEDIA = '/media/pi/'

camera = PiCamera()
shutter_button = Button(20)

mounted_dirs = os.listdir( MEDIA )

# check for a writable USB drive, use the first one found
if( len( mounted_dirs ) > 0 and os.access( MEDIA + mounted_dirs[0], os.W_OK ) ):
    OUT = MEDIA + mounted_dirs[0] + '/' # write to removable drive
else:
    OUT = HM # no USB drive write locally

def capture():

    # datetime contains special characters which fail removable drive writes
    timestamp = datetime.now().strftime("%Y%m%d.%H%M%S") # strip all specials

    filename = OUT + '%s.jpg' % timestamp 
    camera.capture( filename )
    

shutter_button.when_held = camera.start_preview
shutter_button.when_released = camera.stop_preview

shutter_button.when_pressed = capture

pause()


