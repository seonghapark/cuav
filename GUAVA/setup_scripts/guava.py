#!/usr/bin/python3

import sys
import os
import subprocess

master_uri = input("input master ip(main device) : ")

command1 = "export ROS_MASTER_URI=http://"+master_uri+":11311/"
command4 = "ifconfig | grep 192"

my_ip_raw = subprocess.check_output(command4, shell=True)
my_ips = my_ip_raw.split()
my_ip = my_ips[1].decode('utf-8')
print("Hello! Your IP is : " + my_ip[5:])

command2 = "export ROS_HOSTNAME="+my_ip
command3 = "export ROS_IP="+my_ip

os.system(command2)
os.system(command3)

print("URI Setting is done.")
