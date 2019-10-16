#!/usr/bin/env python3

import sys
import os
import time
import rospy
from radar.msg import raw

EXCHANGE_NAME = 'radar'
data = bytearray()

if __name__ == '__main__':
    rospy.init_node('fake_data', anonymous=True)
    fake_data = rospy.Publisher('raw', raw, queue_size=1)
    print('Connect ROS')
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
        for i in range(int(len(read_data)//11724)):
            #print(i)
            raw_data.num = i
            raw_data.data = read_data[i * 11724:(i + 1) * 11724]
            #print(raw_data.num)
            #print(raw_data.data)
            fake_data.publish(raw_data)
            time.sleep(0.1)

    except (KeyboardInterrupt, Exception) as ex:
        print(ex)
    finally:
        print('Close all')
        file.close()