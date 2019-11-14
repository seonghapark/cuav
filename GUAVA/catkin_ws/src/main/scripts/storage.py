#!/usr/bin/env python3

#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String
from datetime import datetime
from radar.msg import raw
from cv_bridge import CvBridge, CvBridgeError
import time
import cv2
from main.msg import realtime
from main.msg import result
from main.msg import result_web
from DecisionClass import DecisionClass
from main_log import log_generator



# from main.msg import result


def callback_final_result(data, args):
	pub_log = args[0]
	pub_web = args[1]
	DecisionValues = DecisionClass(data.coords_camera, data.percent_camera, data.percent_radar, data.image_camera, data.image_radar, data.direction)
	fileName = time.strftime("%Y%m%d_%H%M%S")
	DecisionValues.image_camera_name = fileName + '_radar.jpg'
	DecisionValues.image_radar_name = fileName + '_camera.jpg'

	directory = '/home/project/cuav/GUAVA/catkin_ws/src/main/storage/final_result/'
	image_data_camera = open(directory + fileName + '_camera_data.txt', 'wb')
	image_data_radar = open(directory + fileName + '_radar_data.txt', 'wb')

	bridge = CvBridge()

	# publish/subscribe log
	log = log_generator('storage',"Get Message From <final_result> topic",'sub')
	pub_log.publish(log)
	print(log)

	# assign the value from parameter(message) to local variable
	try:
		cv_image_camera = bridge.imgmsg_to_cv2(data.frame, desired_encoding="passthrough")
		cv_image_radar = bridge.imgmsg_to_cv2(data.frame, desired_encoding="passthrough")
		cv2.imwrite(directory + DecisionValues.image_camera_name, cv_image_camera)
		cv2.imwrite(directory + DecisionValues.image_radar_name, cv_image_radar)
	except CvBridgeError as e:
		print(e)

	print("coordinates : ", data.coords_camera, file=image_data_camera)
	print("percent : ", data.percent_camera, file=image_data_camera)

	print("percent : ", data.percent_radar, file=image_data_radar)

	image_data_camera.close()
	image_data_radar.close()

	web_message = DecisionValues.generate_web_message()
	pub_web.publish(web_message)

	# publish/subscribe log
	log = log_generator('storage',"Send Message to <web_result> topic",'pub')
	pub_log.publish(log)
	print(log)




# raw data from raw topic in radar
def callback_raw(data,args):
	pub_log = args
	fileNmae = time.strftime("%Y%m%d_%H%M%S") + '_binary.txt'
	directory = '/home/project/cuav/GUAVA/catkin_ws/src/main/logs/storage/raw/'
	binary_data = open(directory+fileNmae, 'wb')

	received_data = bytearray()
	received_data = data.data

	lengthMSb = bytes([11025 >> 8])
	lengthLSb = bytes([11025 & 0xFF])
	binary_data.write(lengthMSb + lengthLSb + data)
	binary_data.close()

	# log
	log = log_generator('storage', 'raw data file from radar <' + fileNmae + '> is saved.')
	pub_log.publish(log)
	print(log)




def callback_realtime_result(data,args):
	pub_log = args
	fileName = time.strftime("%Y%m%d_%H%M%S")
	directory = '/home/project/cuav/GUAVA/catkin_ws/src/main/storage/camera_image/'
	image_data = open(directory+fileName+'_data.txt', 'wb')
	bridge = CvBridge()

	# publish/subscribe log
	log = log_generator('storage', "Get Message From <result> topic", 'sub')
	pub_log.publish(log)
	print(log)



	# assign the value from parameter(message) to local variable
	try:
		cv_image = bridge.imgmsg_to_cv2(data.frame, desired_encoding="passthrough")
		cv2.imwrite(directory+fileName+'_image.jpg',cv_image)
	except CvBridgeError as e:
		print(e)

	print("coordinates : ", data.coords, file=image_data)
	print("percent : ", data.percent, file=image_data)

	image_data.close()


def storage(pub_log, pub_web):

	rospy.init_node('storage', anonymous=True)

	# log
	log = log_generator('storage', 'storage node is initialized..')
	print(log)
	pub_log.publish(log)

	rospy.Subscriber('realtime_result', realtime, callback_realtime_result, pub_log)
	rospy.Subscriber('final_result', result, callback_final_result, (pub_log, pub_web))
	#rospy.Subscriber('img_camera', realtime, callback_result, pub_log)
	rospy.Subscriber('raw', raw, callback_raw, pub_log)
	rospy.spin()

if __name__ == '__main__':
	pub_log = rospy.Publisher('logs', String, queue_size=10)
	pub_web = rospy.Publisher('web_result', result_web, queue_size=10)

	storage(pub_log, pub_web)
