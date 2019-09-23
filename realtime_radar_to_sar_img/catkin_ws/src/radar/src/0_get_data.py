#! /usr/bin/env python

from serial import Serial, SerialException
import argparse

import time

import rospy
from radar.msg import raw
from radar.msg import rail

EXCHANGE_NAME = 'radar'
data = bytearray()

def callback(end):
    global data
    print("publish")
    pub = rospy.Publisher('raw', raw, queue_size=10)
    raw_data = raw()

    lengthMSb = bytes([11025 >> 8])
    lengthLSb = bytes([11025 & 0xFF])
    binary_data = lengthMSb + lengthLSb
    data = bytearray()

    raw_data.data = binary_data
    raw_data.num = 1
    pub.publish(raw)

def main(args):
    try:
        rospy.init_node('get_data', anonymous=True)
        rospy.Subscriber('rail', rail, callback)
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
    main(parser.parse_args())
