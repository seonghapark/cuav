#!/bin/bash
. ../../../devel/setup.bash
roscore & 
sleep 2
rosrun main storage.py &
sleep 2
rosrun main web.py &
sleep 2
rosrun camera classifier_camera.py &
sleep 2
rosrun camera get_frame.py --config cfg/yolo-drone.cfg --weight weights/yolo15-drone.weights --labels cfg/coco-drone.names --conf 0.5 --nms 0.4 --resolution 416 &
sleep 2
rosrun camera fake_rail.py &
sleep 2
rosrun main decision.py &
#gnome-terminal -e "rosrun camera classifier_camera.py"
#sleep 2
# gnome-terminal -e "rosrun camera get_frame.py --config cfg/yolo-drone.cfg --weight weights/yolo-drone.weights --labels cfg/coco-drone.names --conf 0.5 --nms 0.4 --resolution 416"
# gnome-terminal -e "rosrun camera get_frame.py --config cfg/yolov3-tiny.cfg --weight weights/yolov3-tiny.weights --labels cfg/coco.names --conf 0.5 --nms 0.4 --resolution 416"
#sleep 2
#gnome-terminal -e "rosrun camera fake_rail.py"
#sleep 2
#gnome-terminal -e "rosrun camera fake_start.py"


