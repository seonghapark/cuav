#! /usr/bin/env python3

import numpy as np
from datetime import datetime
import time

import rospy
from radar.msg import raw, wav, realtime
from std_msgs.msg import String

PACKAGE_NAME = 'radar'
NODE_NAME = 'analyzer'
DATA = bytearray()
SAMPLE_RATE = 5862

rospy.init_node('analyzer', anonymous=True)
pub_wav = rospy.Publisher('wav', wav, queue_size=1)
#pub_realtime_wav = rospy.Publisher('realtime_wav', wav, queue_size=10)
pub_realtime_wav = rospy.Publisher('realtime_wav', realtime, queue_size=100)
log = rospy.Publisher('logs', String, queue_size=100)


class RadarBinaryParser():
    def __init__(self, raw_data, sr=5862):
        self.raw_data = raw_data
        self.sr = sr
        self.sync = None
        self.data = None

    # get sync, data and headers from text binary file.
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
            # sync is True when if first byte's first 3 bits value are 1
            sync.append(True if (data[index] >> 5) == 1 else False)
        self.sync = np.array(sync)
        self.data = np.array(values)

        # print(self.sync, self.data, len(self.sync), len(self.data))
        return self.sync, self.data


class ifft_handler():
    def __init__(self):
        self.opp = 0
        #self.fs = 44100  # Sampling rate
        self.fs = 5862
        self.Tp = 0.020   # Radar ramp up-time
        self.n = int(self.Tp*self.fs)   # Samples per ramp up-time
        self.fsif = np.zeros([10000,self.n], dtype=np.int16)  # Zero array for further data storage

    def dbv(self, input):
        input = input + 0.0000001
        return 20 * np.log10(abs(input))  # Calculate Decibel using received signal intensity value

    def data_process(self, sync, data, num):
        count = 0
        result_time = [] # time is a list
        #self.fs = len(sync)
        self.n = int(self.Tp*self.fs)
        self.fsif = np.zeros([10000,self.n], dtype=np.int16)
        # print(self.fs)

        # print(data, data.shape, self.n)
        # print(sync, sync.shape)

        spliter = 10 # to search rising edge
        val = 2
        for ii in range(val, int((sync.shape[0] - self.n)), spliter):  # improved searching loop
            # if sync[ii - 11 - spliter:ii - spliter] == []:
            #     continue
            if (ii - spliter > 0) & (sync[ii] == True) & (sync[ii - val - spliter:ii - spliter].max() == False):  # if start[ii] is true and the mean of from start[ii-11] to start[ii-1] is zero (All False)
                for jj in range(ii - spliter, ii):
                    if (sync[jj] == True) & (sync[jj - val:jj - 1].mean() == 0.0):
                        # print(data[jj:jj + self.n], jj)
                        # print(self.n)
                        self.fsif[count, :] = data[jj:jj + self.n]  # then copy rightarray from ii to ii+n and paste them to sif[count] --> sif[count] is a list
                        result_time.append((jj + int(sync.shape[0]) * self.opp) * 1. / self.fs)  # append time, the time is ii/fs --> few micro seconds (0.0001 sec or so)
                        count = count + 1

                        self.fsif[count, :] = data[jj + 1:jj + 1 + self.n]  # then copy rightarray from ii to ii+n and paste them to sif[count] --> sif[count] is a list
                        result_time.append((jj + 1 + int(sync.shape[0]) * self.opp) * 1. / self.fs)  # append time, the time is ii/fs --> few micro seconds (0.0001 sec or so)
                        count = count + 1

                        break

        self.opp += 1
        #temp = [x + num for x in result_time]
        result_time = np.array(result_time)  # change the format of time from list to to np.array
        sif = self.fsif[:count,:] # truncate sif --> remove all redundant array lists in sif, just in case if sif is longer then count
        sif = sif - np.tile(sif.mean(0), [sif.shape[0], 1])
        zpad = int(8 * self.n / 2)  # create the number_of_ifft_entities --> which is the number of vales that has to be created from fft calculation
        decibel = self.dbv(np.fft.ifft(sif, zpad, 1)) # Do fft calculation, and convert results to decibel through dbv function
        real_value = decibel[:,0:int(decibel.shape[1] / 2)]
        max_real = real_value.max()
        result_data = real_value - max_real

        #### 2 pulse cancelor RTI plot
        sif2 = sif[1:sif.shape[0],:] - sif[:sif.shape[0]-1,:]
        last = sif[-1,:]
        sif2 = np.vstack((sif2, last))
        # print(sif2, sif2.shape, sif.shape, zpad)
        v = np.fft.ifft(sif2, zpad, 1)
        decibel = self.dbv(v)
        real_value = decibel[:,0:int(decibel.shape[1] / 2)]
        max_real = real_value.max()
        result_data = real_value - max_real

        result_time = result_time[:50]
        result_data = result_data[:50]

        # print(result_time.dtype, result_data.dtype)
        return result_time, result_data


def publish_realtime_wav(data):
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'SUB', str_time, 'Subscribe from realtime')
    log.publish(log_text)
    print(log_text)

    ifft = ifft_handler()
    raw_data = raw()
    raw_data.data = data.data
    raw_data.num = data.num
    print("data num : ", data.num, " data len : ", len(raw_data.data))

    parser = RadarBinaryParser(raw_data.data, sr=SAMPLE_RATE)
    sync, real_data = parser.parse()
    print("After Parsing\nsync : ", sync.shape, type(sync), "data : ", real_data.shape, type(real_data))

    if sync is None:
        time.sleep(0.2)

    st = time.time() * 1000
    result_time, result_data = ifft.data_process(sync, real_data, raw_data.num)  # It takes approximately 500 ms
    et = time.time() * 1000

    str_time = str(datetime.now()).replace(' ', '_')
    str_msg = 'After IIFT Data : ' + str(result_data.shape) + ' Sync : ' + str(result_time.shape)
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, str_msg)
    log.publish(log_text)
    print(log_text)
    print(result_time.dtype, type(result_time), result_time)

    wav_data = realtime()
    #wav_data.data = result_data.astype(np.float64)
    #wav_data.sync = result_time.astype(np.float64)
    wav_data.data = result_data.tostring()
    wav_data.sync = result_time.tostring()
    print(type(wav_data.data), len(wav_data.data))
    wav_data.num = raw_data.num
    # wav_data.sr = SAMPLE_RATE

    pub_realtime_wav.publish(wav_data)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'PUB', str_time, 'Publish to realtime_wav')
    log.publish(log_text)
    print(log_text)


def publish_wav(data):
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'SUB', str_time, 'Subscribe from raw')
    log.publish(log_text)
    print(log_text)

    str_msg = 'Data num : ' + str(data.num) + 'Data len : ' + str(len(data.data))
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, str_msg)
    log.publish(log_text)
    print(log_text)

    raw_data = raw()
    raw_data.data = data.data
    raw_data.num = data.num
    # parse text binary file
    parser = RadarBinaryParser(raw_data.data, sr=SAMPLE_RATE)
    sync, data = parser.parse()
    #print("sync : ", sync.shape, type(sync), sync.dtype, "data : ", data.shape, type(data), data.dtype)

    str_time = str(datetime.now()).replace(' ', '_')
    str_msg = 'Data : ' + str(data.shape) + ' Sync : ' + str(sync.shape)
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, str_msg)
    log.publish(log_text)
    print(log_text)
    print('################################')
    print(sync)

    wav_data = wav()
    wav_data.data = data.astype(np.uint16)
    wav_data.sync = sync.astype(np.uint16)
    wav_data.num = raw_data.num
    wav_data.sr = SAMPLE_RATE

    # Publish Audio Numpy data
    pub_wav.publish(wav_data)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'PUB', str_time, 'Publish to wav')
    log.publish(log_text)
    print(log_text)


def listener():
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, 'analyzer connects ROS')
    log.publish(log_text)
    print(log_text)

    rospy.Subscriber('raw', raw, publish_wav)
    rospy.Subscriber('realtime', raw, publish_realtime_wav)
    rospy.spin()


if __name__ == '__main__':
    listener()