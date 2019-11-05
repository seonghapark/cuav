#!/usr/bin/env python3

import sys
import os
import time
import rospy
from radar.msg import raw
from std_msgs.msg import String

rospy.init_node('fake_data', anonymous=True)
fake_data = rospy.Publisher('raw', raw, queue_size=1)
log = rospy.Publisher('log', String, queue_size=10)
EXCHANGE_NAME = 'radar'
DATA = bytearray()

if __name__ == '__main__':
    #rospy.init_node('fake_data', anonymous=True)
    #fake_data = rospy.Publisher('raw', raw, queue_size=1)
    print('Connect ROS')
    log.publish('Connect ROS')
    raw_data = raw()

    # read file
    pwd = os.getcwd()# current working folder
    # file_name = pwd+ '/' +sys.argv[1]
    file_name = sys.argv[1]
    file = open(file_name, "rb")
    read_data = file.read()
    read_data = bytearray(read_data)
    print('file read')

    try:
        # divide input
        print(len(read_data)//11724)
        for I in range(int(len(read_data) // 11724)):
            #print(i)
            raw_data.num = I
            raw_data.data = read_data[I * 11724:(I + 1) * 11724]
            #print(raw_data.num)
            #print(raw_data.data)
            fake_data.publish(raw_data)
            time.sleep(0.1)

    except (KeyboardInterrupt, Exception) as ex:
        print(ex)
    finally:
        print('Close all')
        file.close()