#! /usr/bin/env python3
from serial import Serial, SerialException
import argparse

import time
from datetime import datetime

import rospy
from radar.msg import raw, railstart, railstop
from std_msgs.msg import String

package_name = 'radar'
node_name = 'receiver'
str_time = str(datetime.now()).replace(' ', '_')
log = rospy.Publisher('log', String, queue_size=10)
data = bytearray()
flag = False
start_radar = bool()
i = 0

def callback2(rail):
    global data, start_radar, i
    start_radar = False

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'SUB', str_time, 'Subscribe from railstop')
    log.publish(log_text)

    pub = rospy.Publisher('raw', raw, queue_size=1)
    raw_data = raw()

    raw_data.data = data
    raw_data.num = i

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'Data num : ', i, ' Data length : ', len(data))
    log.publish(log_text)

    i += 1
    data = bytearray()

    pub.publish(raw_data)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'PUB', str_time, 'Publish to raw')
    log.publish(log_text)


def callback1(start, args):
    global flag, start_radar

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'SUB', str_time, 'Subscribe from start')
    log.publish(log_text)

    pub_operate = rospy.Publisher('operate', railstart, queue_size=1)
    operate = railstart()
    operate.start = True

    if not flag:
        operate.direction = True
        flag = True
    else:
        operate.direction = False
        flag = False

    pub_operate.publish(operate)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'PUB', str_time, 'Publish to operate')
    log.publish(log_text)

    #rail starts moving, get data from radar
    start_radar = True
    with Serial(args.device, 115200) as serial:
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'Begin receiving')
        log.publish(log_text)

        while start_radar:
            if serial.inWaiting() > 0:
                data.extend(serial.read(serial.inWaiting()))
            else:
                time.sleep(0.01)
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'End receiving')
        log.publish(log_text)


def listener(args):
    rospy.init_node('receiver', anonymous=True)
    rospy.Subscriber('start', String, callback1, (args))
    rospy.Subscriber('terminate', railstop, callback2)
    rospy.spin()


if __name__ == '__main__':
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'receiver connects ROS')
    log.publish(log_text)

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', dest='device', help='Device path')

    listener(parser.parse_args())
