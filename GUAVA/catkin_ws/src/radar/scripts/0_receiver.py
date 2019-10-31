#! /usr/bin/env python3
from serial import Serial, SerialException
import argparse

import time
from datetime import datetime
from threading import Thread

import rospy
from radar.msg import raw
from main.msg import operate
from std_msgs.msg import String

package_name = 'radar'
node_name = 'receiver'
data = bytearray()
flag = bool()
i = 0


def callback2(operate, log):
    global data, flag, i
    flag = False

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'SUB', str_time, 'Subscribe from end')
    print(log_text)
    log.publish(log_text)

    pub = rospy.Publisher('raw', raw, queue_size=1)
    raw_data = raw()

    raw_data.data = data
    raw_data.num = i

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'Data num : ', i, ' Data length : ', len(data))
    print(log_text)
    log.publish(log_text)

    i += 1
    data = bytearray()

    pub.publish(raw_data)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'PUB', str_time, 'Publish to raw')
    print(log_text)
    log.publish(log_text)


def callback1(operate, args):
    global flag
    log = args[0]

    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'SUB', str_time, 'Subscribe from operate : start')
    print(log_text)
    log.publish(log_text)

    #rail starts moving, get data from radar
    flag = True
    with Serial(args[1].device, 115200) as serial:
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'Begin receiving')
        print(log_text)
        log.publish(log_text)

        while flag:
            if serial.inWaiting() > 0:
                data.extend(serial.read(serial.inWaiting()))
            else:
                time.sleep(0.01)
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'End receiving')
        print(log_text)
        log.publish(log_text)


def listener(args):
    rospy.init_node('receiver', anonymous=True)

    log = rospy.Publisher('log', String, queue_size=10)
    str_time = str(datetime.now()).replace(' ', '_')
    log_text = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'receiver connects ROS')
    print(log_text)
    log.publish(log_text)

    rospy.Subscriber('operate', operate, callback1, (log, args))
    rospy.Subscriber('end', operate, callback2, (log))
    rospy.spin()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', dest='device', help='Device path')

    listener(parser.parse_args())
