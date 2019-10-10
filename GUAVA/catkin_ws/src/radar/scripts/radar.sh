#!/bin/bash
. ../../../devel/setup.bash
gnome-terminal -e "roscore"
sleep 3
#gnome-terminal -e "make_sar_image.py"
#gnome-terminal -e "rosrun radar 3_draw.py"
#sleep 3
gnome-terminal -e "rosrun radar 2_analyzer.py"
sleep 3
#gnome-terminal -e "rosrun radar 0_get_data.py"
gnome-terminal -e "rosrun radar fake_data_sender.py ../../../20181114_180324_binary.txt"
