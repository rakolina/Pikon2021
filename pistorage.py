#! /usr/bin/python

# rsync originals from local storage to USB drive
# safe mode - originals need to be removed by user
# destroy mode: --remove-source-files passed to rsync command

import logging
import json
import os
from signal import pause

MODE = '' # do not remove originals unless config file specifically says so
DESTROY = '--remove-source-files'

HM = '/home/pi/Pikon2021/'
LCL = '/home/pi/Pictures/'
MEDIA = '/media/pi/'

LOG = HM + 'pistorage.log'
FMT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig( filename=LOG, encoding='utf-8', format=FMT, level=logging.CRITICAL )

# MAIN 

# read options json file
CONF = HM + 'pishutter.conf'
if( os.path.isfile( CONF ) ):
    with open(CONF, 'r') as jsonfile:
        logging.info( 'config file: ' + CONF )
        data = json.load(jsonfile)
        jsonfile.close()
else:
    logging.critical('Fatal. Config file not found. Exit')
    exit( -1 )


# update from config setting
if( 'logging' in data ):
    if( data['logging'] == 'error' ):
        logging.basicConfid( level = logging.ERROR )
    elif( data['logging'] == 'warning' ):
        logging.basicConfid( level = logging.WARNING )
    elif( data['logging'] == 'info' ):
        logging.basicConfid( level = logging.INFO )
    elif( data['logging'] == 'debug' ):
        logging.basicConfid( level = logging.DEBUG )

if( 'mode' in data and data['mode'] == 'destroy' ):
    MODE = DESTROY


# check for a writable USB drive, use the first one found
while( true ):
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
        sleep( 3000 ) # TODO verify time unit, sleep for 3 seconds
    



