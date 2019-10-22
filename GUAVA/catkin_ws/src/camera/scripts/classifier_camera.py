import cv2
import rospy
from std_msgs.msg import String, Bool
from camera.msg import sendframe
from cv_bridge import CvBridge, CvBridgeError


class ClassifierCamera:
	def __init__(self):
		self.detected_frames = []
		self.detected_objects = []
		self.detected_percentages = []

	def preprocess_frames(self):
		try:
			for o, p in zip(self.detected_objects, self.detected_percentages):
				print(o,p)
			return self.detected_frames[0], self.detected_objects[0], self.detected_percentages[0]
		except EOFError:
			print("Error")

	def realtime_callback(self, frame_data):
		print("Send frame in realtime")
		realtime_frame = rospy.Publisher('realtime_camera', sendframe, queue_size=10)

		# accumulate detected frames + labels + percentages
		cv_image = CvBridge.imgmsg_to_cv2(frame_data.frame, "bgr8")
		cv2.imshow("YOLO", cv_image)
		print(frame_data.object)
		print(frame_data.percentage)
		self.detected_frames.append(cv_image)
		self.detected_objects.append(frame_data.object)
		self.detected_percentages.append(frame_data.percentage)

	def summary_callback(self, send_summary):
		if send_summary:
			print("Send summarized frame")
			summary_frame = rospy.Publisher('summary_camera', sendframe, queue_size=10)
			send_data = sendframe()

			# preprocess summarized data
			frame, send_data.object, send_data.percentage = self.preprocess_frames()
			send_data.frame = CvBridge.cv2_to_imgmsg(frame, "bgr8")  # encoding="passthrough",

			print("SUMMARY CALLBACK")
			print(send_data.object)
			print(send_data.percentage)

			# publish summarized data
			summary_frame.publish(send_data)

			# empty data
			self.detected_frames.clear()
			self.detected_objects.clear()
			self.detected_percentage.clear()


if __name__ == '__main__':
	classifier_camera = ClassifierCamera()
	rospy.init_node('classifier_camera', anonymous=True)
	rospy.Subscriber('img_camera', sendframe, classifier_camera.realtime_callback)
	rospy.Subscriber('operate', Bool, classifier_camera.summary_callback)
	rospy.spin()


