#! /usr/bin/python

# Continuosly read from the momentary button
# when pressed, get current date 
# and create a new photo image, name it 
# {timestamp}.jpg and save it in /home/pi
# or on a removable USB drive if available

import logging
import json
import os

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

HM='/home/pi/Pikon2021/'
OUT = '/home/pi/Pictures/'
MEDIA = '/media/pi/'

LOG = HM + 'pishutter.log'
FMT = 
logging.basicConfig(filename=LOG, encoding='utf-8',
        format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

logging.info( 'pishutter.py starting' )

camera = PiCamera()
shutter_button = Button( 20 )
preview_button = Button( 21 )


# FUNCTIONS    

def setup_storage():

    # check for a writable USB drive, use the first one found
    if( os.path.isdir ( MEDIA ) ):
        mounted_dirs = os.listdir( MEDIA )
        if( len( mounted_dirs ) > 0 and os.access( MEDIA + mounted_dirs[0], os.W_OK ) ):
            OUT = MEDIA + mounted_dirs[0] + '/' # write to removable drive

    logging.info( 'storage set to: ' + OUT )


def read_config():

    # read camera options configuration json file
    CONF = HM + 'pishutter.conf'
    if( os.path.isfile( CONF ) ):
        with open(CONF, 'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
    else:
        logging.error('Fatal error. Config file not found. Exiting')
        exit( -1 )


def capture():

    # datetime contains special characters which fail removable drive writes
    timestamp = datetime.now().strftime("%Y%m%d.%H%M%S") # strip all specials

    filename = OUT + '%s.jpg' % timestamp 
    camera.capture( filename )
    logging.info( 'saving image: ' + filename )
    

# MAIN

setup_storage
read_config

preview_button.when_held = camera.start_preview
preview_button.when_released = camera.stop_preview

shutter_button.when_pressed = capture
 
pause()


