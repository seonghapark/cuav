#!/usr/bin/env python3

import cv2
import rospy
from std_msgs.msg import String
from camera.msg import sendframe
from cv_bridge import CvBridge, CvBridgeError
from camera_log import log_generator


class ClassifierCamera:
	def __init__(self):
		self.classify = rospy.Subscriber('img_camera', sendframe, self.callback)
		self.realtime = rospy.Publisher('realtime_camera', sendframe, queue_size=3)
		self.summary = rospy.Publisher('summary_camera', sendframe, queue_size=3)
		self.log = rospy.Publisher('log', String, queue_size=10)
		self.node_name = "classifier_camera"
		self.detected_frames = []
		self.detected_objects = []
		self.detected_percentages = []
		self.bridge = CvBridge()
		self.send_frame = sendframe()
		self.log.publish(log_generator(self.node_name, "classifier_camera connects ROS"))

	def callback(self, data):
		if data.operate == "start":
			self.log.publish(log_generator(self.node_name, "img_camera(rail operating)", "sub"))
			self.realtime_callback(data)
		elif data.operate == "end":
			self.log.publish(log_generator(self.node_name, "img_camera(rail ended)", "sub"))
			pass
			# self.summary_callback(data)

	def preprocess_frames(self):
		try:
			for o, p in zip(self.detected_objects, self.detected_percentages):
				print(o, p)
			return self.detected_frames[0], self.detected_objects[0], self.detected_percentages[0]
		except EOFError:
			print("EOF error")

	def realtime_callback(self, frame_data):
		self.realtime.publish(frame_data)
		self.log.publish(log_generator(self.node_name, "realtime_camera", "pub"))
		try:
			cv_image = self.bridge.imgmsg_to_cv2(frame_data.frame, desired_encoding="passthrough")
		except CvBridgeError as e:
			print(e)

		cv2.imshow("classify Frame", cv_image)
		cv2.waitKey(10)

		# accumulate detected frames + labels + percentages
		self.detected_frames.append(cv_image)
		self.detected_objects.append(frame_data.object)
		self.detected_percentages.append(frame_data.percent)

	def summary_callback(self, frame_data):
		# preprocess summarized data
		frame, self.send_frame.object, self.send_frame.percent = self.preprocess_frames()

		try:   
			self.send_frame.operate = frame_data.operate
			self.send_frame.frame = self.bridge.cv2_to_imgmsg(frame, encoding="passthrough")
			self.summary.publish(self.send_frame)
			self.log.publish(log_generator(self.node_name, "summary_camera", "pub"))
		except CvBridgeError as e:
			print(e)

		print("SUMMARY CALLBACK")

		# empty data
		self.detected_frames.clear()
		self.detected_objects.clear()
		self.detected_percentages.clear()


if __name__ == '__main__':
	classifier_camera = ClassifierCamera()
	rospy.init_node('classifier_camera', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shut down - keyboard interruption")

