#!/usr/bin/env python3
import cv2
import sys
import rospy
import argparse
from detection_boxes import DetectBoxes
from std_msgs.msg import String
from camera.msg import sendframe
from cv_bridge import CvBridge, CvBridgeError
from camera_log import log_generator
from main.msg import operate
import time

def arg_parse():
    """ Parsing Arguments for detection """

    parser = argparse.ArgumentParser(description='Yolov3')
    parser.add_argument("--config", help="Yolov3 config file", default="cfg/yolo-drone.cfg")
    parser.add_argument("--weight", help="Yolov3 weight file", default="weights/yolo-drone.weights")
    parser.add_argument("--labels", help="Yolov3 label file", default="cfg/coco-drone.names")
    parser.add_argument("--conf", dest="confidence", help="Confidence threshold for predictions",
                        default=0.5, type=float)
    parser.add_argument("--nms", dest="nmsThreshold", help="NMS threshold",
                        default=0.4, type=float)
    parser.add_argument("--resolution", dest='resol',
                        help="Input resolution of network. Higher resolution increases accuracy but decreases speed",
                        default=416, type=int)
    return parser.parse_args()


class GetFrame:
    def __init__(self, node_name, log_pub):
        self.operate = rospy.Subscriber('operate', operate, self.callback)
        self.pub_frame = rospy.Publisher('img_camera', sendframe, queue_size=3)
        self.log = log_pub
        self.node_name = node_name
        self.net = None
        self.detect = None
        self.cap = None
        self.args = arg_parse()
        self.frame_data = sendframe()
        self.bridge = CvBridge()

    def callback(self, data):
        if data.command == "init":
            print("data.command == init")
            self.log.publish(log_generator(self.node_name, "operate(camera - initialized)", "sub"))
            self.initialize()
        elif data.command == "start":
            print("data.command == start")
            self.log.publish(log_generator(self.node_name, "operate(rail operating)", "sub"))
            self.get_frame(data)
        elif data.command == "end":
            print("data.command == end")
            self.log.publish(log_generator(self.node_name, "operate(rail ended)", "sub"))
            self.get_frame(data)

    def initialize(self):
        self.log.publish(log_generator(self.node_name, "Loading network....."))
        self.net = cv2.dnn.readNetFromDarknet(self.args.config, self.args.weight)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        self.log.publish(log_generator(self.node_name, "Network successfully loaded"))

        # load DetectBoxes class
        self.detect = DetectBoxes(self.args.labels,
                                  confidence_threshold=self.args.confidence,
                                  nms_threshold=self.args.nmsThreshold)
        
        try:
            self.cap = cv2.VideoCapture(0)
            self.log.publish(log_generator(self.node_name, "Webcam initialized"))
        except IOError:
            self.log.publish(log_generator(self.node_name, "No Webcam detected - system exits"))
            sys.exit(1)

    @staticmethod
    def get_outputs_names(net):
        # names of network layers e.g. conv_0, bn_0, relu_0....
        layer_names = net.getLayerNames()
        return [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    def get_frame(self, operate):
        # if start signal came before init signal
        # initialize net & camera
        if self.cap is None or not self.cap.isOpened():
            self.initialize()

        i = 0
        while self.cap.isOpened():
            has_frame, frame = self.cap.read()

            # if end of frame, program is terminated
            if not has_frame:
                break

            # Create a 4D blob from a frame.
            blob = cv2.dnn.blobFromImage(frame, 1 / 255, (self.args.resol, self.args.resol),
                                         (0, 0, 0), True, crop=False)

            # Set the input to the network
            self.net.setInput(blob)

            # Runs the forward pass
            network_output = self.net.forward(self.get_outputs_names(self.net))

            # Extract the bounding box and draw rectangles
            self.frame_data.percent, self.frame_data.coords = self.detect.detect_bounding_boxes(frame, network_output)

            # Efficiency information
            t, _ = self.net.getPerfProfile()
            elapsed = abs(t * 1000.0 / cv2.getTickFrequency())
            label = 'Time per frame : %0.0f ms' % elapsed
            cv2.putText(frame, label, (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

            print("FPS {:5.2f}".format(1000/elapsed))

            # publish frames + detected objects
            if i == 5:
                self.frame_data.operate = "end"
            else:
                self.frame_data.operate = operate.command
            try:
                self.frame_data.frame = self.bridge.cv2_to_imgmsg(frame, encoding="passthrough")
                self.pub_frame.publish(self.frame_data)
                self.log.publish(log_generator(self.node_name, "img_camera", "pub"))
            except CvBridgeError as e:
                print(e)

            i += 1

        self.log.publish(log_generator(self.node_name, "Camera closed"))
        # releases video and removes all windows generated by the program
        # cap.release()


if __name__ == '__main__':
    rospy.init_node('get_frame', anonymous=True)
    log = rospy.Publisher('logs', String, queue_size=10)
    log.publish(log_generator('get_frame', "Start get_frame"))
    g_frame = GetFrame('get_frame', log)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shut down - keyboard interruption")
