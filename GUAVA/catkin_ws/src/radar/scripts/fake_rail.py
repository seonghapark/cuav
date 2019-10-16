#! /usr/bin/env python3

import rospy
from radar.msg import railstop

rospy.init_node("fake_rail")
pub = rospy.Publisher('terminate', railstop, queue_size=1)
rate = rospy.Rate(0.05)
message = railstop()
message.terminate = True
while not rospy.is_shutdown():
    print("rail end")
    pub.publish(message)
    rate.sleep()
