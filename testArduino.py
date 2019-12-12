import serial
from threading import *
import serial.tools.list_ports
from arduino import *

# port_list = list(serial.tools.list_ports.comports())
# for i in port_list:
#    print(i.device)
a = arduino()
a.init()
a.start()
