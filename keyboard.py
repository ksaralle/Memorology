from threading import *
import sys



class keyboard(Thread):
    def init(self):
        self.input = ""
        self.rawInput = ""
    def run (self):
        while True:
            print("keyboard running.")
            read = False
            if sys.stdin.isatty():
                #print ("data received.")
                for line in sys.stdin:
                    self.rawInput = line
                    self.input = line[:(len(line)-1)]
                    
            else:
                print("no data")
