#! /usr/bin/env python
import sys
from scipy.io import wavfile
import os

from serial import Serial, SerialException
import argparse
# import pika

import time
import numpy as np

import struct

import rospy
from radar.msg import raw
from radar.msg import rail
EXCHANGE_NAME = 'radar'

data = bytearray()

# class ros_communication():
def callback(end):
    global data
    pub = rospy.Publisher('raw', raw, queue_size=10)
    raw_data = raw()

    lengthMSb = bytes([11025 >> 8])
    lengthLSb = bytes([11025 & 0xFF])
    binary_data = lengthMSb + lengthLSb
    data = bytearray()

    raw_data.data = binary_data
    raw_data.num = 1
    pub.publish(raw)

# rail end signal
def listener(self):
    rospy.init_node('get_data', anonymous=True)
    rospy.Subscriber('rail', rail, callback)
    rospy.spin()

def main(args):
    try:
        print('begin receiving...')
        with Serial(args.device, 115200) as serial:
            while True:
                if serial.inWaiting() > 0:
                    data.extend(serial.read(serial.inWaiting()))
                else:
                    time.sleep(0.01)
    except (KeyboardInterrupt, Exception) as ex:
        print(ex)
    finally:
        print('Close all')(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', dest='device', help='Device path')
    listener()
    main(parser.parse_args())
