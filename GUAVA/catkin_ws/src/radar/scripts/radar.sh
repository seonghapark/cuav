#!/bin/bash
. ../../../devel/setup.bash
sudo chmod 777 /dev/ttyACM0
gnome-terminal -e "roscore"
sleep 1
gnome-terminal -e "rosrun radar make_sar_image.py"
sleep 1
#gnome-terminal -e "rosrun radar 3_draw.py"
#sleep 1
gnome-terminal -e "rosrun radar 2_analyzer.py"
sleep 1
gnome-terminal -e "rosrun radar 0_get_data.py -d /dev/ttyACM0"
#gnome-terminal -e "rosrun radar fake_data_sender.py ../test_data/with_plate.txt"
sleep 1
gnome-terminal -e "rosrun radar fake_rail.py"
sleep 2
gnome-terminal -e "rosrun main fake_start.py"