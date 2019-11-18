#!/bin/bash
killall -9 roscore
. ../../../devel/setup.bash
sudo chmod 777 /dev/ttyACM0
#gnome-terminal -e "roscore"
#sleep 1
rosrun radar make_sar_image.py & 
sleep 2
rosrun radar 3_plotter.py & 
sleep 2
rosrun radar 2_analyzer.py &
sleep 2
rosrun radar 0_receiver.py -d /dev/ttyACM0 &

#gnome-terminal -e "rosrun radar make_sar_image.py"
#sleep 1
#gnome-terminal -e "rosrun radar 3_plotter.py"
#sleep 1
#gnome-terminal -e "rosrun radar 2_analyzer.py"
#sleep 1
#gnome-terminal -e "rosrun radar 0_receiver.py -d /dev/ttyACM0"
#gnome-terminal -e "rosrun radar 1-1_r_read_data.py ../test_data/20191111_170312_binary.txt"
#sleep 1
#gnome-terminal -e "rosrun main fake_start.py"
