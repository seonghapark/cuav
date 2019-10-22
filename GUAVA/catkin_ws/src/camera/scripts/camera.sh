#!/bin/bash
. ../../../devel/setup.bash
gnome-terminal -e "roscore"
sleep 1
gnome-terminal -e "rosrun camera classifier_camera.py"
sleep 1
gnome-terminal -e "rosrun camera get_frame.py --config cfg/yolov3-drone.cfg --weight weights/yolov3-drone.weights --labels cfg/coco-drone.names --conf 0.5 --nms 0.4 --resolution 416"
sleep 1
gnome-terminal -e "rosrun radar fake_rail.py"
sleep 2
gnome-terminal -e "rosrun main fake_start.py"