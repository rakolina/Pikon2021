#! /usr/bin/python

# Continuosly read from the momentary button
# when long-pressed shutdown the Pi

import os
from gpiozero import Button
from signal import pause

def shutdown():
    os.system( "shutdown now -h" )

shutdown_button = Button( 21, hold_time = 2 )    
shutdown_button.when_held = shutdown

pause()


