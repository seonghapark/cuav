#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from threading import Thread
from std_msgs.msg import String
#from camera.msg import msgname

def get_frame():
	pub = rospy.Publisher('img', String, queue_size=1) # need to change String to msgname
	rospy.init_node('get_frame', anonymous=True)
	rate = rospy.Rate(10)
	
	print("node initialized..")
	
	### Get Frame from Raspberry Pi Camera Module ###
	#                                               #
        #      code for getting frame  will be here     #
	#                                               #
	#################################################

	### fill the message for pulish to classifier_camera node ###
	# data = msgname()                                          #
	# data.img = imgbyte..                                      #
	# ......                                                    #
	#############################################################

	### publish message ###
	# pub.publish(data)

def callback_start(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	print("start get_frame")
	get_frame()

if __name__ == '__main__':

	rospy.Subscriber('start', start, callback_start)
	rospy.spin()
