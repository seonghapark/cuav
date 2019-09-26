#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from threading import Thread
from std_msgs.msg import String

status = [False, False]

def callback_radar(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	status[0] = True
def callback_camera(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	status[1] = True
def is_ready(pub_storage, pub_web):
	i = 0
	while status[0] == False or status[1] == False:
		if i%8000000==0:
			print("waiting results...")
		i += 1
	#if two results are received...
	
	### processing results... ###

	#in later.. the type is not String type. that will be change to custom message type
	rate = rospy.Rate(10)
	result_message = "done!"
	rospy.loginfo("storage! I'm " + result_message)
	rospy.loginfo("web! I'm " + result_message)
	
	pub_storage.publish("storage!, I'm " + result_message)
	pub_web.publish("web!, I'm " + result_message)
	rate.sleep()
	

def decision():
	pub = rospy.Publisher('start', String, queue_size=10)
	rospy.init_node('decision', anonymous=True)
	rate = rospy.Rate(10)
	#while not rospy.is_shutdown():
	start_message = "Let's get it! current time : %s" % rospy.get_time()
	rospy.loginfo(start_message)
	pub.publish(start_message)
	rate.sleep()

	rospy.Subscriber('result_radar', String, callback_radar)
	rospy.Subscriber('result_camera', String, callback_camera)

	rospy.spin()

if __name__ == '__main__':
	
	pub_storage = rospy.Publisher('result_storage', String, queue_size=10)
	pub_web = rospy.Publisher('result_web', String, queue_size=10)
	
	th2 = Thread(target=is_ready,args=(pub_storage,pub_web))

	#th1.start()
	th2.start()
	#th1.join()
	decision()
	th2.join()

	
	
