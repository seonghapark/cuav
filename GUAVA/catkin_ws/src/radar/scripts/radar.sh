#!/bin/bash
. ../../../devel/setup.bash
gnome-terminal -e "roscore"
sleep 3
gnome-terminal -e "rosrun radar make_sar_image.py"
sleep 3
#gnome-terminal -e "rosrun radar 3_draw.py"
#sleep 3
gnome-terminal -e "rosrun radar 2_analyzer.py"
sleep 3
#gnome-terminal -e "rosrun radar 0_get_data.py"
gnome-terminal -e "rosrun radar fake_data_sender.py ../test_data/with_plate.txt"
