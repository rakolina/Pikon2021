#! /usr/bin/python

# Continuosly read from the momentary button
# when long-pressed shutdown the Pi

from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_button = Button( 21, hold_time = 2 )    
shutdown_button.when_held = shutdown

pause()


