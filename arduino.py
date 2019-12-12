import serial
from threading import *
import serial.tools.list_ports

# port_list = list(serial.tools.list_ports.comports())
# for i in port_list:
#    print(i.device)

class arduino(Thread):
    def init(self):
        self.command = ""
        self.isSystemOn = False
        self.toPlay = False
        self.toRecord = False
        self.delete = False
        self.forward = False
        self.backward = False



    # a -> which reader
    # reader 0 -> play
    # reader 1 -> record

    # a = a.split(b',')[0]
    # a ->  " b'1\r\n' " / " b'0\r\n' "

    # id -> b' F0 AE 37\r\n'


    def run (self):
        with serial.Serial('/dev/ttyUSB0', 9600, timeout=100) as ser:
            while True:

                a = ser.readline()
                print(a)

                if (a == b'mouthPiece up\r\n'):
                    print("picking up mouth piece.")
                    # self.command = "on"
                    self.isSystemOn = True


                elif (a == b'mouthPiece down\r\n'):
                    print("putting down mouth piece.")
                    # self.command = "off"
                    self.isSystemOn = False
                    self.toPlay = False
                    self.toRecord = False

                elif (a == b'play button pressed\r\n'):
                    print("play button pressed. ")
                    self.toPlay = True
                    self.toRecord = False

                elif (a == b'record button pressed\r\n'):
                    print("record button pressed. ")
                    self.toPlay = False
                    self.toRecord = True

                elif (a == b'cancel button pressed\r\n'):
                    print("delete button pressed. ")
                    self.delete = True

                elif (a == b'joystick left\r\n'):
                    print("joystick left. ")
                    self.backward = True

                elif (a == b'joystick right\r\n'):
                    print("joystick right. ")
                    self.forward = True


                else:
                    print("invalid serial input. ")



                #elif (a == b'play'):
                #    self.play = False
                #elif(a==b'play\r\n'):
                #    self.play = True
