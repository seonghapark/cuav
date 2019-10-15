#!/usr/bin/env python3
import sys
import os
import time
import rospy
from radar.msg import raw

def talker():
    pub = rospy.Publisher('raw', raw, queue_size=1)
    rospy.init_node('fake_data_sender', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    # read file
    file_name = sys.argv[1]
    raw_data = raw()
    file = open(file_name, "rb")
    
    data = file.read()
    i = 0
    max_num = int(len(data)//(10000000)) if len(data) > 10000000 else 1
    print('len_data : ', len(data))
    print('max_num', max_num)
    try:
        # divide input
        while not rospy.is_shutdown():

            if len(data) > 10000000 :
                if i<max_num :
                    raw_data.data = data[i*(10000000):(i+1)*(10000000)+1]
                else :
                    raw_data.data = data[i*(10000000):len(data)]

                raw_data.num = i+1
                rospy.loginfo("max_num : " + str(max_num) + " time" + str(i) + ":" + str(rospy.get_time()))
                pub.publish(raw_data)
                rate.sleep()

                if i < max_num :
                    i = i+1
                else :
                    break

            else :
                print('pubbbbbb')
                raw_data.data = data
                raw_data.num = 1
                rospy.loginfo("max_num : " + str(max_num) + " time" + str(i) + ":" + str(rospy.get_time()))
                pub.publish(raw_data)
                break


    except (KeyboardInterrupt, Exception) as ex:
        print(ex)
    finally:
        print('Close all')
        file.close()
        a=input()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
