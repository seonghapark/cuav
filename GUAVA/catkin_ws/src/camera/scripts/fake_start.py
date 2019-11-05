#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

print('fake_start')
rospy.init_node("fake_decision")
pub = rospy.Publisher('operate', String, queue_size=1)
rate = rospy.Rate(5)
message = "init"
print("system start")
while not rospy.is_shutdown():
    rospy.sleep(1)
    pub.publish(message)
    print('init sended')
    rospy.sleep(600)
