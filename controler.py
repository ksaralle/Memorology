import sys

from database import *
# from keyboard import *
from player import player
from recorder import *
from sensor import *                                    
                                                      
(cur,con)= init()


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
#listen press
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







record = None
play = None
light = sensor()
light.init()
light.start()
#keyboard = keyboard()
#keyboard.init()
#keyboard.start()
while True:
    if play != None:
        try:
            if not play.ifdo:
                play.stop()
                play.join()
                print("join player successful")
                play = None
                keyboard.input = ""
        except:
            stopmessage = player()
            stopmessage.init("./audio/no.wav")
            stopmessage.start()
            while stopmessage.ifdo:
                None
            stopmessage.stop()
            stopmessage.join()
            play = None
            keyboard.input = ""
    if record != None:
        if not record.isPlay:
            record.stop()
            record.join()
            record = None
            keyboard.input = ""
    if ( light.play and keyboard.input != ""):
        if play == None:
            search1(keyboard.input)
    elif((not light.play) and (not light.record) and keyboard.input != ""):
        if play!= None:
            play.stop()
            play.join()
            print("join player successful")
            play = None
            keyboard.input = ""
    if (light.record and keyboard.input != ""):
        if record == None:
            search2(keyboard.input)
    elif((not light.record) and (not light.play) and keyboard.input != ""):
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
            keyboard.input = ""
    
    