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
