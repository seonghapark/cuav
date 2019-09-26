#! /usr/bin/env python3

import numpy as np
import sys
from scipy.fftpack import fft
import os
import time
import rospy
from radar.msg import raw, wav
from scipy.io import wavfile

EXCHANGE_NAME = 'radar'
SAMPLE_RATE = 44100

class RadarBinaryParser():
    def __init__(self, raw_data, sr=5862):
        self.raw_data = raw_data
        self.sr = sr
        self.sync = None
        self.data = None

    '''get sync, data and headers from text binary file.
    '''

    def parse(self):
        data = bytearray(self.raw_data)
        # print(len(data))
        # parse the sync and data signal in bytearray

        # length of data is under 2 byte
        if len(data) < 2:
            return None, None #there are no data
        # sync of first data's second bit is over 0
        if (data[0] >> 6) > 0:
            del data[:1] #delete first and second byte
        # length of data is not divided by two
        if len(data) % 2 == 1:
            del data[-1:] #delete last data

        values = []
        sync = []
        for index in range(0, len(data), 2): # read two bytes
            high = data[index] & 0x1F # last five bits of first byte
            low = data[index + 1] & 0x1F # last five bits of second byte
            values.append(high << 5 | low) # concatenate first 5bits + second 5bits = 10 bits
            #sync is True when if first byte's first 3 bits value are 1
            sync.append(True if (data[index] >> 5) == 1 else False)
        self.sync = np.array(sync)
        self.data = np.array(values)

        # print(self.sync, self.data, len(self.sync), len(self.data))
        return self.sync, self.data

def callback(data):
    print('raw data received')
    raw_data = raw()
    raw_data.data = data.data
    raw_data.num = data.num
    # parse text binary file
    parser = RadarBinaryParser(raw_data.data, sr=SAMPLE_RATE)
    sync, data = parser.parse()
    print('data : ',data.shape)
    print(data)
    print('sync : ',sync.shape)
    print(sync)
    # stacking audio data
    #audio = np.vstack((sync,data))
    #audio = audio.T.astype(np.int16)
    #rospy.loginfo(audio)

    wav_data = wav()
    wav_data.data = data.astype(np.uint8)
    wav_data.sync = sync.astype(np.uint8)
    wav_data.num = raw_data.num
    wav_data.sr = SAMPLE_RATE
    # Publish Audio Numpy data
    pub = rospy.Publisher('wav',wav,queue_size=1)
    print(wav_data.data, wav_data.sync)
    pub.publish(wav_data)

def listener():
    rospy.init_node('analyzer',anonymous=True)
    rospy.Subscriber('raw',raw,callback)
    rospy.spin()

if __name__ == '__main__':
    #print('Connect RMQ')
    #rabbitmq = rmq_commumication()
    print('Connect ROS')
    listener()

