import cv2
import sys
import rospy
import argparse
import numpy as np
from detection_boxes import DetectBoxes
from std_msgs.msg import String
from camera.msg import sendrealtime
from cv_bridge import CvBridge, CvBridgeError



def arg_parse():
    """ Parsing Arguments for detection """

    parser = argparse.ArgumentParser(description='Yolov3')
    parser.add_argument("--video", help="Path where video is located",
                        default="assets/drone_video_short.mp4", type=str)
    parser.add_argument("--config", help="Yolov3 config file", default="cfg/yolov3-drone.cfg")
    parser.add_argument("--weight", help="Yolov3 weight file", default="weights/yolov3-drone.weights")
    parser.add_argument("--labels", help="Yolov3 label file", default="cfg/coco-drone.names")
    parser.add_argument("--conf", dest="confidence", help="Confidence threshold for predictions", default=0.5)
    parser.add_argument("--nms", dest="nmsThreshold", help="NMS threshold", default=0.4)
    parser.add_argument("--resolution", dest='resol', help="Input resolution of network. Higher "
                                                      "increases accuracy but decreases speed",
                        default="416", type=str)
    return parser.parse_args()


def get_outputs_names(net):
    # names of network layers e.g. conv_0, bn_0, relu_0....
    layer_names = net.getLayerNames()
    return [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


def get_frame():
    args = arg_parse()

    pub = rospy.Publisher('img_camera', sendrealtime, queue_size=100)
    frame_data = sendrealtime()

    # rate = rospy.Rate(10) # not sure this is necessary
    bridge = CvBridge()

    print("Loading network.....")
    net = cv2.dnn.readNetFromDarknet(args.config, args.weight)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    print("Network successfully loaded")

    # load detection class, default confidence threshold is 0.5
    detect = DetectBoxes(args.labels, confidence_threshold=args.confidence, nms_threshold=args.nmsThreshold)

    try:
        cap = cv2.VideoCapture(0)
        print("Start reading image frames from Webcam")
    except IOError:
        print("No webcam")
        sys.exit(1)

    while cap.isOpened():
        hasFrame, frame = cap.read()
        # if end of frame, program is terminated
        if not hasFrame:
            break

        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(frame, 1 / 255, (int(args.resol), int(args.resol)), (0, 0, 0), True,
                                     crop=False)

        # Set the input to the network
        net.setInput(blob)

        # Runs the forward pass
        network_output = net.forward(get_outputs_names(net))

        # Extract the bounding box and draw rectangles
        frame_data.object, frame_data.percentage = detect.detect_bounding_boxes(frame, network_output)

        # Efficiency information
        t, _ = net.getPerfProfile()
        elapsed = abs(t * 1000.0 / cv2.getTickFrequency())
        label = 'Time per frame : %0.0f ms' % elapsed
        cv2.putText(frame, label, (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

        print("FPS {:5.2f}".format(1000/elapsed))

        # save image frames
        frame = np.uint8(frame)
        frame_data.frame = bridge.cv2_to_imgmsg(frame, "bgr8") # encoding="passthrough",
        pub.publish(frame_data)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Camera detection ended")
    # releases video and removes all windows generated by the program
    cap.release()
    # Terminate if no more camera detection available
    callback_end()


def callback_start(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print("start get_frame")
    get_frame()


def callback_end(data):
    sys.exit(1)


if __name__ == '__main__':
    rospy.init_node('get_frame', anonymous=True)
    rospy.Subscriber('start', String, callback_start)
    rospy.spin()
    # main node 전체 종료 subscribe
    # rospy.Subscriber('terminate', railstop, callback_end)


