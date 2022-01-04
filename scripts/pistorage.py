#! /usr/bin/python

# rsync originals from local storage to USB drive
# safe mode - originals need to be removed by user
# destroy mode: images are moved onto USB drive and originals are deleted 

import json
import os
import time

<<<<<<< HEAD
MODE = '' # do not remove originals unless config file specifically says so
DESTROY = '--remove-source-files'

=======
>>>>>>> 5bfce555c45b3828e19cc83d763f22516719af42
HM = '/home/pi/Pikon2021/'
LCL = '/home/pi/Pictures/'
MEDIA = '/media/pi/'
RSYNC = '/usr/bin/rsync'
DESTROY = ''
DEBUG = 1

# read options json file
CONF = HM + 'pistorage.conf'
if( os.path.isfile( CONF ) ):
    with open( CONF, 'r' ) as jsonfile:
        if ( 1 == DEBUG ):
            print ( 'config file: ' + CONF )
        data = json.load(jsonfile)
        jsonfile.close()
else:
    if ( 1 == DEBUG ):
        print ('Fatal. Config file not found. Exit')
    exit( -1 )

if( 'mode' in data and data['mode'] == 'destroy' ):
    MODE = DESTROY


<<<<<<< HEAD
# check for a writable USB drive, use the first one found
while( true ):
=======
while True:
    # check for a writable USB drive, use the first one found
>>>>>>> 5bfce555c45b3828e19cc83d763f22516719af42
    if( os.path.isdir ( MEDIA ) ):
        mounted_dirs = os.listdir( MEDIA )
        if( len( mounted_dirs ) > 0 and os.access( MEDIA + mounted_dirs[0], os.W_OK ) ):
            OUT = MEDIA + mounted_dirs[0] + '/' # write to removable drive
<<<<<<< HEAD
            args = [ '/usr/bin/rsync', '-av', MODE, LCL, OUT ] 
            logging.info ( 'Executing: ' + ' '.join( args ) )
            subprocess.call( args )
            logging.info( 'Completed moving files onto removable drive ' + OUT )
        else: 
            logging.critical( 'No writable media available' )
    else:
        sleep( 3000 ) # TODO verify time unit, sleep for 3 seconds
    



=======
            args = [ RSYNC, DESTROY, LCL, OUT ] 
            subprocess.call( args )
        else: 
            if ( 1 == DEBUG ):
                print ( 'remote media is not writable' )
    else:
        if ( 1 == DEBUG ):
            print ( 'remote media does not exist' )

    time.sleep( 5 ) # seconds
>>>>>>> 5bfce555c45b3828e19cc83d763f22516719af42
