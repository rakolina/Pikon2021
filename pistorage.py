#! /usr/bin/python

# rsync originals from local storage to USB drive
# safe mode - originals need to be removed by user
# destroy mode: images are moved onto USB drive and originals are deleted 

import json
import os
import time

HM = '/home/pi/Pikon2021/'
LCL = '/home/pi/Pictures/'
MEDIA = '/media/pi/'
RSYNC = '/usr/bin/rsync'
DESTROY = ''
DEBUG = 1

# read options json file
CONF = HM + 'pishutter.conf'
if( os.path.isfile( CONF ) ):
    with open( CONF, 'r' ) as jsonfile:
        if ( 1 == DEBUG ):
            print ( 'config file: ' + CONF )
        data = json.load(jsonfile)
        jsonfile.close()
else:
    f ( 1 == DEBUG ):
        print ('Fatal. Config file not found. Exit')
    exit( -1 )

if( 'mode' in data and data['mode'] == 'destroy' ):
    DESTROY = '--remove-source-files'


while True:
    # check for a writable USB drive, use the first one found
    if( os.path.isdir ( MEDIA ) ):
        mounted_dirs = os.listdir( MEDIA )
        if( len( mounted_dirs ) > 0 and os.access( MEDIA + mounted_dirs[0], os.W_OK ) ):
            OUT = MEDIA + mounted_dirs[0] + '/' # write to removable drive
            args = [ RSYNC, DESTROY, LCL, OUT ] 
            subprocess.call( args )
        else: 
            if ( 1 == DEBUG ):
                print ( 'No writable media available' )
    else:
        if ( 1 == DEBUG ):
            print ( OUT + ' does not exist' )

    time.pause( 5 )
