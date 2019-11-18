#! /usr/bin/env python3
from serial import Serial, SerialException
import argparse

import time
from datetime import datetime

import rospy
from radar.msg import raw
from main.msg import operate
from std_msgs.msg import String

PACKAGE_NAME = 'radar'
NODE_NAME = 'receiver'
DATA = bytearray()
FLAG = bool()
I = 0
realtime_cnt = 0
binary_data = None
sample_rate = 5862

rospy.init_node('receiver', anonymous=True)
log = rospy.Publisher('logs', String, queue_size=10)
pub_raw = rospy.Publisher('raw', raw, queue_size=1)
realtime = rospy.Publisher('realtime', raw, queue_size=10)

end_time = time.time()
start_time = time.time()

def publish(operate):
    global DATA, FLAG, I, realtime_cnt, binary_data, end_time, start_time

    FLAG = False

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'SUB', str_time, 'Subscribe from end')
    print(log_text)
    log.publish(log_text)

    #pub = rospy.Publisher('raw', raw, queue_size=1)
    raw_data = raw()
    raw_data.data = DATA
    raw_data.num = I

    str_time = str(datetime.now()).replace(' ', '_')
    msg = 'Data num : ' + str(I) + ', Data length: ' + str(len(DATA))
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, msg)
    print(log_text)
    log.publish(log_text)

    I += 1
    realtime_cnt = 0

    end_time = time.time()

    lengthMSb = bytes([11025 >> 8])
    lengthLSb = bytes([11025 & 0xFF])
    binary_data.write(lengthMSb + lengthLSb + DATA)
    binary_data.close()
    DATA = bytearray()
    print("#"*50)
    print("Time estimated :", end_time - start_time)
    pub_raw.publish(raw_data)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'PUB', str_time, 'Publish to raw')
    log.publish(log_text)
    print(log_text)


def start(operate, args):
    global FLAG, DATA, realtime_cnt, binary_data, start_time

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'SUB', str_time, 'Subscribe from operate : start')
    print(log_text)
    log.publish(log_text)

    #rail starts moving, get data from radar
    FLAG = True

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, 'Begin receiving')
    print(log_text)
    log.publish(log_text)

    fileName = '../test_data/'+ time.strftime("%Y%m%d_%H%M%S") + '_binary.txt'
    binary_data = open(fileName,'wb')   # Create a file

    start_time = time.time()
    with Serial(args.device, 115200) as serial:
        while FLAG:
            if serial.inWaiting() > 0:
                DATA.extend(serial.read(serial.inWaiting()))
            else:
                time.sleep(0.01)

            current_time = time.time()
            if current_time - start_time > 1.0:
                if len(DATA) >= sample_rate*2:
                    raw_data = raw()
                    raw_data.data = DATA[(sample_rate*2) * realtime_cnt : (sample_rate*2) * (realtime_cnt + 1)]
                    raw_data.num = realtime_cnt
                    realtime.publish(raw_data)
                    realtime_cnt += 1

                    str_time = str(datetime.now()).replace(' ', '_')
                    log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'PUB', str_time, 'Publish to realtime')
                    log.publish(log_text)
                    print(log_text)

                start_time = current_time

        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, 'End receiving')
        log.publish(log_text)
        print(log_text)


def listener(args):
    #rospy.init_node('receiver', anonymous=True)

    #log = rospy.Publisher('log', String, queue_size=10)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, 'receiver connects ROS')
    log.publish(log_text)
    print(log_text)

    rospy.Subscriber('operate', operate, start, (args))
    rospy.Subscriber('end', operate, publish)
    rospy.spin()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', dest='device', help='Device path')

    listener(parser.parse_args())
