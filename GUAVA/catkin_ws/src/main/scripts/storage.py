#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String
from datetime import datetime
# from main.msg import result

def callback_result(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	
	# assign the value from parameter(message) to local variable #
	#							     #
	# class = data.class					     #
	# img = data.img					     #
	# ....							     #
	##############################################################

	# make file for backup
	
	now = datetime.now() # current time for filename
	f = open('/home/project/cuav/GUAVA/catkin_ws/src/main/storage/'+str(now)+'.dat','w')
	test_str = ["for test", "teeeeest"]
	test_str.append(data.data)
	f.write('\n'.join(test_str))
	f.close()

def storage():
	rospy.init_node('storage', anonymous=True)
	rospy.Subscriber('result', String, callback_result)
	rospy.spin()

if __name__ == '__main__':
	storage()
