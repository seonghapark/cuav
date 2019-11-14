#!/bin/bash
. ../../../devel/setup.bash
roscore & 
sleep 2
rosrun main web.py &
