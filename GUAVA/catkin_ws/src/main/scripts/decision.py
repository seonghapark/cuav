#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def decision():
	pub = rospy.Publisher('start', String, queue_size=10)
	rospy.init_node('decision', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		start_message = "Let's get it! current time : %s" % rospy.get_time()
		rospy.loginfo(start_message)
		pub.publish(start_message)
		rate.sleep()

		rospy.Subscriber('result_radar', String, callback)
		rospy.Subscriber('result_camera', String, callback)

		rospy.spin()

if __name__ == '__main__':
	decision()
	
