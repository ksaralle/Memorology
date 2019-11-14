from sensor import *
from threading import *
import serial.tools.list_ports

#port_list = list(serial.tools.list_ports.comports())
#for i in port_list:
#    print(i.device)



light = sensor()
light.init()
light.start()