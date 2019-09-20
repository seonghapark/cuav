#! /usr/bin/env python

import rospy
from radar.msg import rail

rospy.init_node("fake_rail")
pub = rospy.Publisher('rail',rail,queue_size=1)
rate = rospy.Rate(0.5)
message = rail()
message.end = True
while not rospy.is_shutdown():
    pub.publish(message)
    rospy.sleep()
