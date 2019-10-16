#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

print('fake_start')
rospy.init_node("fake_start")
pub = rospy.Publisher('start', String, queue_size=1)
rate = rospy.Rate(0.05)
message = "hello"
while not rospy.is_shutdown():
    print("system start")
    pub.publish(message)
    rate.sleep()
