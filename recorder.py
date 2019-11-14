import pickle
import pymysql
import wave
import pyaudio
import matplotlib.pyplot as plt
import sys
from threading import *
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

class recorder(Thread):
    def init(self,filename):
        self.filename = filename
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        self.frames = []
        self.ifdo = True
        self.isPlay = False
    def run (self):
        print("* in recording")
        self.isPlay = True
        while self.isPlay:
            data = self.stream.read(CHUNK)
            self.frames.append(data)
        # self.isPlay is false:
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.isPlay = False
        print("end recording")
    def stop (self):
        self.isPlay=False
        self.ifdo = False
        print("* done recording, stop now. ")










    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #     data = stream.read(CHUNK)
    #     frames.append(data)
