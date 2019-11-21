#!/bin/bash
# killall -9 roscore
. ../../../devel/setup.bash
#sudo chmod 777 /dev/ttyACM0
#gnome-terminal -e "roscore"
#sleep 1
gnome-terminal -e "rosrun radar make_sar_image.py"
sleep 3
#gnome-terminal -e "rosrun radar 3_plotter.py"
#sleep 1
gnome-terminal -e "rosrun radar 2_analyzer.py"
sleep 3
#gnome-terminal -e "rosrun radar 0_receiver.py -d /dev/ttyACM0"
#gnome-terminal -e "rosrun radar 1-1_r_read_data.py ../test_data/20191111_170312_binary.txt"
gnome-terminal -e "rosrun radar 1_read_data.py ../test_data/20191120_193611_binary.txt"
#gnome-terminal -e "rosrun radar 1_read_data.py ../test_data/20191119_drone_on_chair_indoor.txt"
#sleep
#gnome-terminal -e "rosrun main fake_start.py"
