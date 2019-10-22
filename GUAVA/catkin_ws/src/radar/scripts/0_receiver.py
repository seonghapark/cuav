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
directory = '/home/project/cuav/GUAVA/catkin_ws/src/radar/logs/receiver/'
file_name = directory + str_time + '_' + package_name + '_' + node_name + '.log'
f = open(file_name, 'w')
data = bytearray()
flag = False
start_radar = bool()
i = 0

def callback2(rail):
    global data, start_radar, i
    start_radar = False

    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'SUB', str_time, 'Subscribe from railstop')
    print(log, file=f)

    pub = rospy.Publisher('raw', raw, queue_size=1)
    raw_data = raw()

    raw_data.data = data
    raw_data.num = i

    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'Data num : ', i, ' Data length : ', len(data))
    print(log, file=f)

    i += 1
    data = bytearray()

    pub.publish(raw_data)
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'PUB', str_time, 'Publish to raw')
    print(log, file=f)


def callback1(start, args):
    global flag, start_radar

    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'SUB', str_time, 'Subscribe from start')
    print(log, file=f)

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
    log = '[{}/{}][{}][{}] {}'.format(package_name, node_name, 'PUB', str_time, 'Publish to operate')
    print(log, file=f)

    #rail starts moving, get data from radar
    start_radar = True
    with Serial(args.device, 115200) as serial:
        str_time = str(datetime.now()).replace(' ', '_')
        log = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'Begin receiving')
        print(log, file=f)
        while start_radar:
            if serial.inWaiting() > 0:
                data.extend(serial.read(serial.inWaiting()))
            else:
                time.sleep(0.01)
        str_time = str(datetime.now()).replace(' ', '_')
        log = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'End receiving')
        print(log, file=f)


def listener(args):
    rospy.init_node('receiver', anonymous=True)
    rospy.Subscriber('start', String, callback1, (args))
    rospy.Subscriber('terminate', railstop, callback2)
    rospy.spin()
    f.close()


if __name__ == '__main__':
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format(package_name, node_name, str_time, 'receiver connects ROS')
    print(log)
    print(log, file=f)

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', dest='device', help='Device path')

    listener(parser.parse_args())
