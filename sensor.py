import serial
from threading import *
import serial.tools.list_ports

# port_list = list(serial.tools.list_ports.comports())
# for i in port_list:
#    print(i.device)

class sensor(Thread):
    def init(self):
        self.play = False
        self.record = False
        self.tagID = ""


    def run (self):
        with serial.Serial('/dev/cu.usbserial-1430', 9600, timeout=100) as ser:
            while True:
                a = ser.readline()
                # a -> which reader
                # reader 0 -> play
                # reader 1 -> record

                # a = a.split(b',')[0]
                # a ->  " b'1\r\n' " / " b'0\r\n' "

                # id -> b' F0 AE 37\r\n'


                if (a == b'0\r\n'):
                # play
                    print("reader 0")
                    n = ser.readline()
                    self.tagID = str(n)[3:14]

                    print("ID: ")
                    print(self.tagID)
                    self.play = True
                    self.record = False

                elif(a == b'1\r\n'):
                # record


                    print("reader 1")
                    n = ser.readline()
                    self.tagID = str(n)[3:14]
                    print("ID: ")
                    print(self.tagID)
                    self.play = False
                    self.record = True

                else:
                    print("not reader 0 not reader 1, something is wrong. ")
                    print(a)


                #elif (a == b'play'):
                #    self.play = False
                #elif(a==b'play\r\n'):
                #    self.play = True
