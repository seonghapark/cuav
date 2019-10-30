#!/bin/bash
. ../../../devel/setup.bash
roscore &
sleep 5
# gnome-terminal -e "rosrun camera classifier_camera.py"
# sleep 2
gnome-terminal -e "rosrun camera get_frame.py --config cfg/yolo-drone.cfg --weight weights/yolo-drone.weights --labels cfg/coco-drone.names --conf 0.5 --nms 0.4 --resolution 416"
sleep 2
gnome-terminal -e "rosrun camera fake_rail.py"
sleep 1
gnome-terminal -e "rosrun camera fake_start.py"
#roscore &
#sleep 5
#rosrun camera get_frame.py --config cfg/yolo-drone.cfg --weight weights/yolo-drone.weights --labels cfg/coco-drone.names --conf 0.5 --nms 0.4 --resolution 416 &
# sleep 2
# rosrun camera fake_rail.py &
# sleep 2
# rosrun camera fake_start.py &
