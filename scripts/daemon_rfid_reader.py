#!/usr/bin/env python2

import subprocess
import os
import time
from Reader import Reader

reader = Reader()

# get absolute path of this script
dir_path = os.path.dirname(os.path.realpath(__file__))

print dir_path
while True:
        # reading the card id
        # NOTE: it's been reported that KKMOON Reader might need the following line altered.
        # Instead of:
        # cardid = reader.reader.readCard()
        # change the line to:
        # cardid = reader.readCard()
        # See here for (German ;) details:
        # https://github.com/MiczFlor/RPi-Jukebox-RFID/issues/551
        cardid = reader.reader.readCard()
        try:
            # start the player script and pass on the cardid
            if cardid != None:
                rc = subprocess.call([dir_path + '/rfid_trigger_play.sh --cardid=' + cardid], shell=True)
                print rc
                if rc == 0:
                  while cardid != None:
#                    print cardid
                    time.sleep(2)
                    cardid = reader.reader.checkCard()
                    cardid = reader.reader.checkCard()
#                    print cardid
                  subprocess.call([dir_path + '/playout_controls.sh -c=playerpause'], shell=True)
        except OSError as e:
            print "Execution failed:" 
