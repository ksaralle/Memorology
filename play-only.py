import sys
from database import *
# from keyboard import *
from player import player
from recorder import *
from sensor import *

# 1. play only
# once starts playing, it cant be manually stopped
# 2. play audio only once.
# 3. player audio from database

noRecordingfound = "./audio/no.wav"
recordingCanceled = "./audio/cancel.wav"

(cur,con)= initializeDB()
# make sure database memorology exist

recorderObject = None
# recorder thread
playerObject = None
# player thread

reader = sensor()
reader.init()
reader.start()



def playAudio(filepath):
    temp = player()
    temp.init(str(filepath))
    temp.start()
    while temp.ifdo:
        None
    temp.stop()
    reader.play = False
    temp.join()

# play the corresponding audio from mysql database
def playFromDatabase(id):

    cmd = "select audio from recordings where id = '%s'" % str(id)
    cur.execute(cmd)

    selectedAudioFilePath = str(cur.fetchone());
    selectedAudioFilePath = selectedAudioFilePath[2:(len(selectedAudioFilePath)-3)]
    # selected audio file path:
    # id -> 82 F0 AE 37
    # ('./audio/SpaceOddity.wav',)
    print(selectedAudioFilePath)

    if not selectedAudioFilePath:
        # no audio is found relating to selected id
        playAudio(noRecordingfound)

    else:
        # audio found
        playAudio(selectedAudioFilePath)



# while the program is running
while True:

    if (playerObject == None) :
        if (reader.play):
        # user made an attempt to use the play function
        # needs to start player
            print("trying to play......")
            playFromDatabase(reader.tagID)
            continue
        else:
        # nothing is playing, nor did user make a request
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
            reader.record = False
    else:
        # TBD
        continue
