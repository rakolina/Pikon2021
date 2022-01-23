#! /usr/bin/python

# rsync originals from local storage to USB drive
# safe mode - originals need to be removed by user
# destroy mode: images are moved onto USB drive and originals are deleted 

import json
import os
import time

MODE = '' # do not remove originals unless config file specifically says so
DESTROY = '--remove-source-files'

HM = '/home/pi/Pikon2021/'
LCL = '/home/pi/Pictures/'
MEDIA = '/media/pi/'
RSYNC = '/usr/bin/rsync'

# read options json file
CONF = HM + '/conf/pistorage.conf'
if( os.path.isfile( CONF ) ):
    with open( CONF, 'r' ) as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
else:
    print ('Fatal. Config file not found. Exit')
    exit( -1 )

if( 'mode' in data and data['mode'] == 'destroy' ):
    MODE = DESTROY


while True:
    # check for a writable USB drive, use the first one found
    if( os.path.isdir ( MEDIA ) ):
        mounted_dirs = os.listdir( MEDIA )
        if( len( mounted_dirs ) > 0 and os.access( MEDIA + mounted_dirs[0], os.W_OK ) ):
            OUT = MEDIA + mounted_dirs[0] + '/' # write to removable drive
            args = [ '/usr/bin/rsync', '-av', MODE, LCL, OUT ] 
            logging.info ( 'Executing: ' + ' '.join( args ) )
            subprocess.call( args )
            logging.info( 'Completed moving files onto removable drive ' + OUT )
        else: 
            logging.critical( 'No writable media available' )
    else:
        time.sleep( 5 ) # TODO verify time unit, sleep for 3 seconds
    



