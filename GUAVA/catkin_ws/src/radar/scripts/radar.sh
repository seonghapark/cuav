#!/bin/bash
killall -9 roscore
. ../../../devel/setup.bash
sudo chmod 777 /dev/ttyACM0
#gnome-terminal -e "roscore"
#sleep 1
rosrun radar make_sar_image.py & 
sleep 3 
#rosrun radar 3_plotter.py & 
#sleep 3
rosrun radar 2_analyzer.py &
sleep 3 
#rosrun radar 0_receiver.py -d /dev/ttyACM0 &
rosrun radar 1_read_data.py ../test_data/20191120_193611_binary.txt
