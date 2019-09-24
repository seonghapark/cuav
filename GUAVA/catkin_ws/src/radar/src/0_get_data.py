#! /usr/bin/env python3
from serial import Serial, SerialException
import argparse

import time

import rospy
from main.msg import start
from radar.msg import raw
from radar.msg import railstart
from radar.msg import railstop

EXCHANGE_NAME = 'radar'
data = bytearray()
flag = False
start_radar = bool()

def callback2(rail):
    global data
    global start_radar
    start_radar = False

    print("publish")
    pub = rospy.Publisher('raw', raw, queue_size=10)
    raw_data = raw()

    lengthMSb = bytes([11025 >> 8])
    lengthLSb = bytes([11025 & 0xFF])
    binary_data = lengthMSb + lengthLSb
    data = bytearray()

    raw_data.data = binary_data
    raw_data.num = 1
    pub.publish(raw_data)

def callback1(start, args):
    global flag
    global start_radar
    print('Start Rail')
    pub_operate = rospy.Publisher('operate', railstart, queue_size=10)

    operate = railstart()
    operate.start = True

    if(flag == False):
        operate.direction = True
        flag = True
    else:
        operate.direction = False
        flag = False
    pub_operate.publish(operate)
    #rail starts moving, get data from radar
    start_radar = True
    with Serial(args.device, 115200) as serial:
        print('begin receiving...')
        while (start_radar):
            if serial.inWaiting() > 0:
                data.extend(serial.read(serial.inWaiting()))
            else:
                time.sleep(0.01)
        print('end receiving')

def main(args):
    rospy.init_node('get_data', anonymous=True)
    rospy.Subscriber('start', start, callback1, (args))
    rospy.Subscriber('terminate', railstop, callback2)
    rospy.spin()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', dest='device', help='Device path')
    main(parser.parse_args())
