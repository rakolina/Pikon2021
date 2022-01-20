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
CONF = HM + 'conf/pikon.conf'
LCL_OUT = '/home/pi/Pictures/'

# Expected configuratio options
RAW = ['yuv', 'rgb', 'rgba', 'bgr', 'bgra']
ENCODED = ['jpeg', 'gif', 'bmp', 'png']
ISO = ['100', '200', '300', '400', '500', '600', '700', '800']
SHUTTER = [0.000001, 10]

# def capture(self, output, format=None, use_video_port=False, resize=None, splitter_port=0, bayer=False, **options):
def capture():
    # datetime contains special characters which fail removable drive writes
    timestamp = datetime.now().strftime("%Y%m%d.%H%M%S") # strip all specials
    filename = LCL_OUT + '%s' % timestamp + '.' + conf_data["format"]
    if conf_data["format"] in ENCODED:
        camera.iso = conf_data["iso"]
    camera.shutter_speed = conf_data["shutter"]
    camera.capture(filename, format=conf_data["format"])


if not os.path.isfile(CONF):
    print ('Fatal. Config file not found. Exit')
    exit( -1 )
else:
    with open( CONF, 'r' ) as jsonfile:
        conf_data = json.load(jsonfile)
        jsonfile.close()


camera = PiCamera()

shutter_button = Button( 20 )
preview_button = Button( 21 )

preview_button.when_held = camera.start_preview
preview_button.when_released = camera.stop_preview

shutter_button.when_pressed = capture
 
pause()

