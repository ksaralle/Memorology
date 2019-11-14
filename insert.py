from database import *
from keyboard import *
(cur,con)= init()
key = keyboard()
key.init()
key.start()
while (key.input == ""):
    None
a = key.input
updat = "update old set audio = './audio/disco.wav' where id = '%s'"
cur.execute(updat%(a))
con.commit()