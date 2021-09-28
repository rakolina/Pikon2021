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
MEDIA = '/media/pi/PIKON/'

camera = PiCamera()
shutter_button = Button(20)

def capture():
  
    # check for USB drive
    if( os.access( MEDIA, os.W_OK ) ):
        OUT = MEDIA # write to removable drive
    else:
        OUT = HM # no USB drive write locally

    # datetime contains special characters which fail removable drive writes
    timestamp = datetime.now().strftime("%Y%m%d.%H%M%S") # strip all specials

    filename = OUT + '%s.jpg' % timestamp 
    camera.capture( filename )
    

shutter_button.when_pressed = capture

pause()


