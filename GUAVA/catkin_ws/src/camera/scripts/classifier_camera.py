#!/usr/bin/env python3

import uuid
import cv2
import rospy
from std_msgs.msg import String
from camera.msg import sendframe, sendsummary
from cv_bridge import CvBridge, CvBridgeError
from camera_log import log_generator
from process_img import ProcessImage


class ClassifierCamera:
	def __init__(self, node_name, log_pub):
		self.classify = rospy.Subscriber('img_camera', sendframe, self.callback)
		self.realtime = rospy.Publisher('realtime_camera', sendframe, queue_size=3)
		self.summary = rospy.Publisher('summary_camera', sendsummary, queue_size=3)
		self.log = log_pub
		self.node_name = node_name
		self.detected_frames = []
		self.detected_percentages = []
		self.detected_coords = []
		self.bridge = CvBridge()
		self.frame_data = sendsummary()
		self.processor = ProcessImage()

	def callback(self, data):
		# if object is detected, convert ros message to cv_frame
		# append data to class variables
		if data.coords:
			self.accumulate_detections(data.frame, data.percent, data.coords)

		if data.operate == "start":
			self.log.publish(log_generator(self.node_name, "img_camera(rail operating)", "sub"))
			self.realtime_callback(data)
		elif data.operate == "end":
			self.log.publish(log_generator(self.node_name, "img_camera(rail ended)", "sub"))
			self.summary_callback()

	# publish subscribed data directly
	def realtime_callback(self, sub_data):
		self.realtime.publish(sub_data)
		self.log.publish(log_generator(self.node_name, "realtime_camera", "pub"))
		print(sub_data.percent, sub_data.coords)

	# process accumulated detection data
	# and the publish summarized information
	def summary_callback(self):
		# process summarized data
		frame, self.frame_data.direction, self.frame_data.percent = \
			self.processor.process_summary(self.detected_frames, self.detected_coords, self.detected_percentages)

		# save image file
		directory = '/home/project/cuav/GUAVA/catkin_ws/src/camera/'
		cv2.imwrite(directory + uuid.uuid1() + '_image.jpg', frame)
		print("image saved")

		try:
			self.frame_data.frame = self.bridge.cv2_to_imgmsg(frame, encoding="passthrough")
			self.summary.publish(self.frame_data)
			self.log.publish(log_generator(self.node_name, "summary_camera", "pub"))
		except CvBridgeError as e:
			print(e)

		# empty data
		self.detected_frames.clear()
		self.detected_percentages.clear()
		self.detected_coords.clear()

	# accumulate detection information
	def accumulate_detections(self, fr, per, cor):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(fr, desired_encoding="passthrough")
		except CvBridgeError as e:
			print(e)

		self.detected_frames.append(cv_image)
		self.detected_percentages.append(per)
		self.detected_coords.append(cor)


if __name__ == '__main__':
	rospy.init_node('classifier_camera', anonymous=True)
	log = rospy.Publisher('logs', String, queue_size=10)
	log.publish(log_generator("classifier_camera", "Start classifier_camera"))
	classifier_camera = ClassifierCamera('classifier_camera', log)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shut down - keyboard interruption")

