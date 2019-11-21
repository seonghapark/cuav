#!/usr/bin/env python3

import sys
import rospy
from radar.msg import raw
from std_msgs.msg import String
from datetime import datetime
import time

PACKAGE_NAME = 'radar'
NODE_NAME = 'fake_data'

rospy.init_node('fake_data', anonymous=True)
fake_data = rospy.Publisher('raw', raw, queue_size=1)
log = rospy.Publisher('logs', String, queue_size=10)
DATA = bytearray()
time.sleep(0.2)
sample_rate = 6300

if __name__ == '__main__':
    # rospy.init_node('fake_data', anonymous=True)
    # fake_data = rospy.Publisher('raw', raw, queue_size=1)
    time.sleep(3)
    print('Connect ROS')
    log.publish('Connect ROS')
    raw_data = raw()

    # read file
    file_name = sys.argv[1]
    file = open(file_name, "rb")
    read_data = file.read()
    DATA = bytearray(read_data)
    str_time = str(datetime.now()).replace(' ', '_')
    msg = 'Data num : ' + str(1) + ', Data length: ' + str(len(DATA))
    log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, msg)
    print(log_text)
    log.publish(log_text)
    try:
        raw_data.num = 1
        raw_data.data = DATA
        raw_data.sr = sample_rate
        fake_data.publish(raw_data)
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'PUB', str_time, 'Publish to raw')
        log.publish(log_text)
        print(log_text)
    except (KeyboardInterrupt, Exception) as ex:
        print(ex)
    finally:
        print('Close all')
        file.close()
