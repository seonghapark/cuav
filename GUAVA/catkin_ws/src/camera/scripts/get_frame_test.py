#!/usr/bin/env python
#-*-coding:utf-8-*-

import cv2
import sys
import rospy
from detection_boxes import DetectBoxes
from threading import Thread
from std_msgs.msg import String
from camera.msg import railstart, railstop, sendframe

start_camera = bool()
camera_imgs = []
detected_objects = []
config = "cfg/yolov3-drone.cfg"
weight = "weights/yolov3-drone.weights"
conf = 0.5
nms = 0.4
resolution = 416
labels = "cfg/coco-drone.names"

def get_outputs_names(net):
	# anmes of network layers e.g. conv_0, bn_0, relu_0....
	layer_names = net.getLayerNames()
	return [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def get_frame():
	pub_operate = rospy.Publisher('operate', railstart, queue_size=10) 
	rate = rospy.Rate(10)

	operate = railstart()
	operate.start = True

	pub_operate.publish(operate)

	start_camera = True
		
	print("Loading network.....")
	net = cv2.dnn.readNetFromDarknet(config, weight)
	net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
	net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
	print("Network successfully loaded")
	
	detect = DetectBoxes(labels, confidence_threshold=conf, nms_threshold=nms)

	try:
		cap = cv2.VideoCapture(0)
	except IOError:
		print("No webcam")
		sys.exit(1)
	
	while cap.isOpened():
		has_frame, frame = cap.read()

		if not has_frame:
			break

		blob = cv2.dnn.blobFromImage(frame, 1/255, (resolution, resolution), (0, 0, 0), True, crop=False)

		net.setInput(blob)

		network_output = net.forward(get_outputs_names(net))

		detected_objects = detect.detect_bounding_boxes(frame, network_output, detected_objects)

		t, _ = net.getPerProfile()
		elapsed = abs(t * 1000.0 / cv2.getTickFrequency())
		label = 'Time per frame : %0.0f ms' % elapsed
		cv2.putText(frame, label, (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

		print("FPS {:5.2f}".format(1000/elapsed))
		
		# save image frames
		camera_imgs.append(frame)
		

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		
	print("Webcam Ended")	
	cap.release()

	


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


def callback_end(data):
	global camera_imgs
	global detected_objects
	start_camera = False
	
	print("publish")
	pub = rospy.Publisher('img_camera', sendframe, queue_size=10)
	frame_data = sendframe()

	frame_data.frame = camera_imgs
	frame_data.object = detected_objects

	camera_imgs = []
	detected_objects = []
	pub.publish(frame_data)


if __name__ == '__main__':	
	rospy.init_node('get_frame', anonymous=True)
	rospy.Subscriber('start', start, callback_start)
	rospy.Subscriber('terminate', railstop, callback_end)
	rospy.spin()
