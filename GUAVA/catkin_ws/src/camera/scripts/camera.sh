#!/bin/bash
. ../../../devel/setup.bash
#roscore &
rosrun camera classifier_camera.py &
sleep 2
rosrun camera get_frame.py --config cfg/yolo-drone.cfg --weight weights/yolo15-drone.weights --labels cfg/coco-drone.names --conf 0.5 --nms 0.4 --resolution 416 &
