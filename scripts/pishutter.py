#! /usr/bin/python

# Continuosly read from the momentary button
# when pressed, get current date 
# and create a new photo image, name it 
# {timestamp}.jpg and save it in /home/pi

import json
import os

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

HM = '/home/pi/Pikon2021/'
CONF = HM + 'conf/pikon.v1.conf'
OUT = '/home/pi/Pictures/'
DEBUG = 1

def capture():
    # datetime contains special characters which fail removable drive writes
    timestamp = datetime.now().strftime("%Y%m%d.%H%M%S") # strip all specials

    filename = '%s.jpg' % timestamp 
    camera.capture( OUT + filename )
    if ( 1 == DEBUG ):
        print ( 'saving: ' + filename )
    

# read camera options configuration json file
if( os.path.isfile( CONF ) ):
    with open( CONF, 'r' ) as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
else:
    print ('Fatal. Config file not found. Exit')
    exit( -1 )

# TODO validate config options


camera = PiCamera()
shutter_button = Button( 20 )
preview_button = Button( 21 )

preview_button.when_held = camera.start_preview
preview_button.when_released = camera.stop_preview

shutter_button.when_pressed = capture
 
pause()

