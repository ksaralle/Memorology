from threading import *
import sys



class keyboard(Thread):
    def init(self):
        self.input = ""
    def run (self):
        while True:
            print("emmm")
            read = False
            if sys.stdin.isatty():
                print ("data received.")
                for line in sys.stdin:
                    self.input = line[:(len(line)-1)]
                    print(len(line))
                    print(line)
            else:
                print("no data")
