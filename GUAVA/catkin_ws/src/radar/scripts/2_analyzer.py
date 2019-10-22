#! /usr/bin/env python3

import numpy as np
from datetime import datetime

import rospy
from radar.msg import raw, wav

package_name = 'radar'
node_name = 'analyzer'
str_time = str(datetime.now()).replace(' ', '_')
directory = '/home/project/cuav/GUAVA/catkin_ws/src/radar/logs/analyzer/'
file_name = directory + str_time + '_' + package_name + '_' + node_name + '.log'
f = open(file_name, 'w')
data = bytearray()
SAMPLE_RATE = 5862


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
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'SUB', str_time, 'Subscribe from raw')
    print(log, file=f)

    log = '[{}/{}][{}] [{}]'.format(package_name, node_name, str_time, 'Data num : ', data.num)
    print(log, file=f)

    pub = rospy.Publisher('wav', wav, queue_size=1)
    raw_data = raw()
    raw_data.data = data.data
    raw_data.num = data.num
    # parse text binary file
    parser = RadarBinaryParser(raw_data.data, sr=SAMPLE_RATE)
    sync, data = parser.parse()

    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'Data : ', data.shape, ' Sync : ', sync.shape)
    print(log, file=f)

    # stacking audio data
    #audio = np.vstack((sync,data))
    #audio = audio.T.astype(np.int16)
    #rospy.loginfo(audio)

    wav_data = wav()
    wav_data.data = data.astype(np.uint16)
    wav_data.sync = sync.astype(np.uint16)
    wav_data.num = raw_data.num
    wav_data.sr = SAMPLE_RATE

    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'wav_data : ', len(wav_data.data),
                                    ' wav_sync : ', len(wav_data.sync))
    print(log, file=f)

    # Publish Audio Numpy data
    pub.publish(wav_data)
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'PUB', str_time, 'Publish to wav')
    print(log, file=f)


def listener():
    rospy.init_node('analyzer',anonymous=True)
    rospy.Subscriber('raw',raw,callback)
    rospy.spin()


if __name__ == '__main__':
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'analyzer connects ROS')
    print(log, file=f)
    listener()