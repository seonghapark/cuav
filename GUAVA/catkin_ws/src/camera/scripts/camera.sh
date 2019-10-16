#!/bin/bash
. ../../../devel/setup.bash
gnome-terminal -e "roscore"
sleep 3
gnome-terminal -e "rosrun camera analyze_frame.py"
sleep 3
gnome-terminal -e "rosrun camera detect.py"
