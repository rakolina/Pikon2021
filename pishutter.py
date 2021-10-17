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

HM = '/home/pi/Pikon2021/'
OUT = '/home/pi/Pictures/'

LOG = HM + 'pishutter.log'
FMT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig( filename=LOG, encoding='utf-8', format=FMT, level=logging.CRITICAL)

logging.info( 'pishutter.py starting' )

def capture():
    # datetime contains special characters which fail removable drive writes
    timestamp = datetime.now().strftime("%Y%m%d.%H%M%S") # strip all specials

    filename = '%s.jpg' % timestamp 
    camera.capture( OUT + filename )
    logging.info( 'saving: ' + filename )
    


# MAIN 

# read camera options configuration json file
CONF = HM + 'pishutter.conf'
if( os.path.isfile( CONF ) ):
    with open(CONF, 'r') as jsonfile:
        logging.info( 'config file: ' + CONF )
        data = json.load(jsonfile)
        jsonfile.close()
else:
    logging.error('Fatal. Config file not found. Exit')
    exit( -1 )

# TODO validate config options

# update logging level based on config setting
if( 'logging' in data ):
    if( data['logging'] == 'error' ):
        logging.basicConfid( level = logging.ERROR )
    elif( data['logging'] == 'warning' ):
        logging.basicConfid( level = logging.WARNING )
    elif( data['logging'] == 'info' ):
        logging.basicConfid( level = logging.INFO )
    elif( data['logging'] == 'debug' ):
        logging.basicConfid( level = logging.DEBUG )

camera = PiCamera()
shutter_button = Button( 20 )
preview_button = Button( 21 )

preview_button.when_held = camera.start_preview
preview_button.when_released = camera.stop_preview

shutter_button.when_pressed = capture
 
pause()

