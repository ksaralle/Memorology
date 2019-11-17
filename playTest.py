import sys
# from keyboard import *
from player import player
from recorder import *
from sensor import *

import sounddevice as sd
print (sd.query_devices())

recorderObject = None
# recorder thread
playerObject = None
# player thread

def simplePlay():
    temp = player()
    temp.init("./audio/no.wav")
    temp.start()
    while temp.ifdo:
        None
    temp.stop()
    temp.join()

# while the program is running
while True:
    i = input("type: ")
    print(i)
    if (playerObject == None) :
        if (i != None):
        # user made an attempt to use the play function
        # needs to start player
            print("trying to play.")
            simplePlay()
            continue
        else:
            pass
    else:
        # already playing
        continue


    if (recorderObject == None):
    # record
        if (reader.record):
        # if user made an attempt to use the record function
            pass
            print("recording function not ready yet.")
