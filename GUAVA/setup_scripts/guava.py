#!/usr/bin/python3

import sys
import os
import socket
import re
import urllib

#master_uri = sys.argv[1]
#ros_ip = sys.argv[2]

master_uri = input("input master ip(main device) : ")
ros_ip = input("input your ip : ")

lan = socket.gethostbyname(socket.gethostname())
print(lan)

command1 = "export ROS_MASTER_URI=http://"+master_uri+":11311/"
command2 = "export ROS_HOSTNAME="+ros_ip
command3 = "export ROS_IP="+ros_ip
