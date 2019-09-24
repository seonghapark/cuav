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
        if len(data) < 2:
            return None, None
        if (data[0] >> 6) > 0:
            del data[:1]
        if len(data) % 2 == 1:
            del data[-1:]

        values = []
        sync = []
        for index in range(0, len(data), 2):
            high = data[index] & 0x1F
            low = data[index + 1] & 0x1F
            values.append(high << 5 | low)
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
    # stacking audio data
    #audio = np.vstack((sync,data))
    #audio = audio.T.astype(np.int16)
    #rospy.loginfo(audio)

    wav_data = wav()
    wav_data.data = data.astype(np.int16)
    wav_data.sync = sync.astype(np.int16)
    wav_data.num = raw_data.num
    wav_data.sr = SAMPLE_RATE
    # Publish Audio Numpy data
    pub = rospy.Publisher('wav',wav,queue_size=1)
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

