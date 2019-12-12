import sys
import os
# from database import *
from keyboard import *
from player import player
from recorder import *
from arduino import *


noRecordingfound = "no.wav"
recordingCanceled = "cancel.wav"
confirmToDelete = "cancel.wav"
deleteConfirmed = "no.wav"

# (cur,con)= initializeDB()
# make sure database memorology exist



ard = arduino()
ard.init()
ard.start()

keyboard = keyboard()
keyboard.init()
keyboard.start()

playlist = []
playFile = ""
playNum = 0


recorderObject = None
# recorder thread
playerObject = None
# player thread


def deleteFile(filename):
    list_dir = os.listdir("./audio")
    for i in list_dir:
        if filename == i:
            f = "./audio/%s" % i
            os.remove(f)
            break



# the entire program wait until this finishes executing
def playAudio(filename):
    filepath = "./audio/" + filename
    playerObject = player()
    playerObject.init(str(filepath))
    playerObject.start()
    while playerObject.ifdo:
        None
    playerObject.stop()
    playerObject.join()


def playAudioList(playlist):
    isPlaying = True

    for i in playlist:
        i = "./audio/" + i


    for j in playlist:
        if (!ard.isSystemOn):
            break
        if (!ard.isLoaded):
            break
        playerObject = player()
        playerObject.init(j)
        playerObject.start()
        while playerObject.ifdo:
            if (!ard.isSystemOn):
                break
            if (!ard.isLoaded):
                break
        playerObject.stop()
        playerObject.join()
    isPlaying = False
    state = 2


def containsRecording(id):
    #filename = "%s.wav" % id
    list_dir = os.listdir("./audio")
    for i in list_dir:
        if id in i:
            return True
    return False


def generateFilename(id):
    if (containsRecording(id)):
        id_audio = []
        list_dir = os.listdir("./audio")
        for i in list_dir:
            if id in i:
                id_audio += [i]
        newID = str(id) + str(len(id_audio))
        newFilename = "%s.wav" % newID
        return newFilename
    else:
        newFilename = "%s.wav" % id
        return newFilename

def playlistFromDirectory(id):
    # play the audio file from local folder

    id_audio = []
    list_dir = os.listdir("./audio")
    for i in list_dir:
        if id in i:
            id_audio += [i]
    return id_audio

# play the corresponding audio from mysql database
# def playFromDatabase(id):
#
#     cmd = "select audio from recordings where id = '%s'" % str(id)
#     cur.execute(cmd)
#
#     selectedAudioFilePath = str(cur.fetchone());
#     selectedAudioFilePath = selectedAudioFilePath[2:(len(selectedAudioFilePath)-3)]
#     # selected audio file path:
#     # id -> 82 F0 AE 37
#     # ('./audio/SpaceOddity.wav',)
#     print(selectedAudioFilePath)
#
#     if not selectedAudioFilePath:
#         # no audio is found relating to selected id
#         playAudio(noRecordingfound)
#
#     else:
#         # audio found
#         playAudio(selectedAudioFilePath)




# while the program is running
while True:
    # mouth piece up
    if ard.isSystemOn:
        # item detected
        if keyboard.input != "":
            # something is already being played
            if playerObject != None:
                # an audio file finished playing
                if !playerObject.ifdo:
                    print("an audio file finished playing")
                    playerObject.stop()
                    playerObject.join()
                    playerObject = None
                    # still more audio files to play
                    if playNum < len(playlist) :
                        # start playing the next file
                        print("start playing the next file")
                        playerObject = player()
                        playFile = playlist[playNum]
                        playerObject.init(playFile)
                        playerObject.start()
                        playNum += 1
                    # has played through all corresponding files
                    else:
                        print("done playing playlist")
                        keyboard.input = ""
                        playlist = []
                        playFile = ""
                        playNum = 0

                # play is not finished
                else:
                    # hang up -> stopped listening
                    if not ard.isSystemOn:
                        playerObject.stop()
                        playerObject.join()
                        playerObject = None
                        keyboard.input = ""
                        playlist = []
                        playFile = ""
                        playNum = 0
                        print("exited when playing")
                    # delete button pressed
                    elif ard.delete:
                        # stop the audio thats currently playing
                        playerObject.stop()
                        playerObject.join()
                        playerObject = None
                        playlist = []

                        # play "confirm to delete?" audio
                        print("confirm to delete?")
                        playAudio(confirmToDelete)
                        # reset the delete to false - waiting for user to confirm
                        ard.delete = False
                        while not ard.delete :
                            None
                        # delete button pressed again - confirmed
                        print("delete confirmed!")
                        deleteFile(playFile)
                        playAudio(deleteConfirmed)
                        ard.delete = False

                    # record button pressed
                    elif ard.record:
                        # stop playing
                        playerObject.stop()
                        playerObject.join()
                        playerObject = None
                        playlist = []
                        playFile = ""
                        print("switch to record")
                        # start recording
                        recorderObject = recorder()
                        recorderObject.init(generateFilename(keyboard.input))
                        recorderObject.start()

                    # joytick pressed right wards
                    elif ard.forward:
                        # stop playing the current file
                        print("next recording")
                        playerObject.stop()
                        playerObject.join()
                        playerObject = None

                        playerObject = player()
                        playNum = min(len(playlist)-1, playNum)
                        playFile = playlist[playNum]
                        playerObject.init(playFile)
                        playerObject.start()
                        playNum += 1


                    # joytick pressed right wards
                    elif ard.backward:
                        print("previous recording")
                        playerObject.stop()
                        playerObject.join()
                        playerObject = None

                        playerObject = player()
                        playFile = playlist[max(0, playNum-1)]
                        playerObject.init(playFile)
                        playerObject.start()



                    # nothing pressed during play
                    else:
                        None


            # is already recording
            elif recorderObject != None:
                # name of this new recording
                # newFile = generateFilename(keyboard.input)

                # hang up to save
                if not ard.isSystemOn:
                    # save
                    print("hangup recording -> saving")
                    recorderObject.stop()
                    recorderObject.join()
                    recorderObject = None
                    keyboard.input = ""
                # delete button pressed
                elif ard.delete:
                    print("cancel this recording?")
                    playAudio(confirmToDelete)
                    ard.delete = False
                    # delete button pressed again - confirmed
                    while ard.delete = False:
                        None
                    # delete button pressed again - confirmed
                    print("cancel recording - confirmed!")
                    recorderObject.stop()
                    recorderObject.join()
                    recorderObject = None
                    deleteFile(generateFilename(keyboard.input))
                    ard.delete = False

                elif ard.toPlay:
                    print("save recording and play immediately")
                    # save recording
                    name = recorderObject.getFileName()
                    recorderObject.stop()
                    recorderObject.join()
                    recorderObject = None
                    # start playing
                    playlist = playlistFromDirectory(keyboard.input)
                    playerObject = player()
                    playerObject.init(name)
                    playerObject.start()
                    playNum = playlist.index(name) + 1



            # no playerObject / not playing
            else:
                # play requested
                if ard.toPlay:
                    if containsRecording(keyboard.input):
                        playlist = playlistFromDirectory(keyboard.input)
                        playNum = 0
                        print("starting playing the playlist")
                        playerObject = player()
                        playerObject.init(playlist[playNum])
                        playerObject.start()
                        playNum += 1

                    else:
                        # no audio found
                        print("no audio file found")
                        playAudio(noRecordingfound)
                        ard.toPlay = False
                # record requested
                elif ard.toRecord:
                        recorderObject = recorder()
                        recorderObject.init(generateFilename(keyboard.input))
                        recorderObject.start()
                # item placed, have not pressed buttons, or pressed invalid buttons
                else:
                    None


        # no keyboard input
        else:
            None
    # is system on  = false
    else:
        None
