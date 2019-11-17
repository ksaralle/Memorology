import sys
from database import *
# from keyboard import *
from player import player
from recorder import *
from sensor import *

(cur,con)= initializeDB()
# make sure database memorology exist

record = None
# recorder thread
play = None
# player thread
reader = sensor()
reader.init()
reader.start()
#keyboard = keyboard()
#keyboard.init()
#keyboard.start()

while True:
    if play != None:
    # if player is already activated
        try:
            # 已经开始播放的情况 detect是否录音已播放完毕
            if not play.ifdo:
            # 不用再play了
                play.stop()
                play.join()
                print("join player successful")
                play = None
                reader.tagID = ""
        except:
            # no audio is found
            stopmessage = player()
            stopmessage.init("./audio/no.wav")
            stopmessage.start()
            while stopmessage.ifdo:
                None
            stopmessage.stop()
            stopmessage.join()
            play = None
            reader.tagID = ""
    if record != None:
        # recorder is already activated
        if not record.isPlay:
        # recording already stopped, .stop() called
            record.stop()
            record.join()
            record = None
            reader.tagID = ""
    if (reader.play and reader.tagID != ""):
        # 正常情况 开始播放
        if play == None:
        # try to find if there is any corresponding audio file to play
            search1(reader.tagID)
    elif((not reader.play) and (not reader.record) and reader.tagID != ""):
    # ???
        if play!= None:
            play.stop()
            play.join()
            print("join player successful")
            play = None
            reader.tagID = ""
            print("mystery case triggered. ")

    if (reader.record and reader.tagID != ""):
    # 正常情况 开始录音
        if record == None:
            search2(reader.tagID)

    elif((not reader.record) and (not reader.play) and reader.tagID != ""):
        if record != None:
            record.stop()
            record.join()
            print("join recorder successful")
            stopmessage = player()
            stopmessage.init("./audio/EndRecord.wav")
            stopmessage.start()
            while stopmessage.ifdo:
                None
            stopmessage.stop()
            stopmessage.join()
            record =None
            reader.tagID = ""


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
            # already contains item, needs to overwrite it
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
            # initiate new item
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
