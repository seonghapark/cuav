#!/usr/bin/env python3
import sys
import os
import time
import rospy
from radar.msg import raw

SAMPLE_RATE = 44100
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
    max_num = int(len(data)//(SAMPLE_RATE*2))
    try:
        # divide input
        while not rospy.is_shutdown():             
            
            if i < max_num-1 : 
                i = i+1 
            else :
                break
            if i<max_num-1 :
                raw_data.data = data[i*(SAMPLE_RATE*2):(i+1)*(SAMPLE_RATE*2)+1]
            else :
                raw_data.data = data[i*(SAMPLE_RATE*2):len(data)]
            
            raw_data.num = i

            rospy.loginfo("max_num : "+str(max_num)+" time"+str(i)+":"+str(rospy.get_time()))
            pub.publish(raw_data)
            
            rate.sleep()

    except (KeyboardInterrupt, Exception) as ex:
        print(ex)
    finally:
        print('Close all')
        file.close()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
