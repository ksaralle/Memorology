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








# find audio file to play for player
def search1(path):
    global play
    play = player()
    cur.execute("select * from old where id ="+str(path))
    infor = cur.fetchall()
    try:
        print("22222")
        audio = infor[0][1]
        print("1111")
        play.init(audio)
        play.start()
    except:
        print("no audio was found")


# find where to store the recording
def search2(path):
    print("in search")
    print("path: " + path)

    global light
    global record
    messagestart  = player()
    record = recorder()
    value = "./audio/{}.wav".format(path)
    print("first created value: " + value)
    cur.execute("select * from old where id ="+str(path))
    infor = cur.fetchall()
    try:
        oldaudio = infor[0][1]
        updat = "update old set audio = '%s' where id = '%s'"
        cur.execute(updat%(value,path))
        messagestart.init("/home/pi/Downloads/cs160FinalProject-master/finalProject/audio/StartRecord.wav")
        messagestart.start()
        while messagestart.ifdo:
            if (not light.record) and (not light.play):
                messagestart.stop()
                cancelmessage = player()
                cancelmessage.init("/home/pi/Downloads/cs160FinalProject-master/finalProject/audio/cancel.wav")
                cancelmessage.start()
                while cancelmessage.ifdo:
                    None
                cancelmessage.stop()
                cancelmessage.join()
        messagestart.stop()
        messagestart.join()
        if light.record:
            record.init(value)
            record.start()
            con.commit()
        else:
            record = None
            keyboard.input = ""
    except:
        sql = "insert into old(id,audio) values( '{}', '{}' )".format(path,value)
        cur.execute(sql)
        messagestart.init("/home/pi/Downloads/cs160FinalProject-master/finalProject/audio/StartRecord.wav")
        messagestart.start()
        while messagestart.ifdo:
            if (not light.record) and (not light.play):
                messagestart.stop()
                cancelmessage = player()
                cancelmessage.init("/home/pi/Downloads/cs160FinalProject-master/finalProject/audio/cancel.wav")
                cancelmessage.start()
                while cancelmessage.ifdo:
                    None
                cancelmessage.stop()
                cancelmessage.join()
        messagestart.stop()
        messagestart.join()
        if light.record:
            print("value: " + value)
            record.init(value)
            record.start()
            con.commit()
        else:
            record = None
            keyboard.input = ""
