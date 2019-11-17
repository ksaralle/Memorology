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
    keyboardInput = input("type: ")
    print(keyboardInput)

    if (playerObject == None) :

        if (keyboardInput == "a"):
        # user made an attempt to use the play function
        # needs to start player
            print("trying to play.")
            #simplePlay()
            continue
        else:
            pass
    else:
        # already playing
        continue


    if (recorderObject == None):
    # record
        if (keyboardInput == "b"):
        # start recording
            filename = "./audio/testing.wav"
            recorderObject = recorder()
            recorderObject.init(filename)
            recorderObject.start()


    else:
        # save recording
        if (keyboardInput == "s"):
            recorderObject.stop();
