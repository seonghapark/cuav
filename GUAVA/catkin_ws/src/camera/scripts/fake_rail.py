#! /usr/bin/env python3

import rospy
from main.msg import operate

print('fake_rail')
rospy.init_node("fake_rail")
pub = rospy.Publisher('operate', operate, queue_size=3)
pub_end = rospy.Publisher('end', operate, queue_size=3)
rate = rospy.Rate(5)
rospy.sleep(10)
op = operate()
op_end = operate()
while not rospy.is_shutdown():
    rospy.sleep(1)
    print("rail start")
    op.command = "start"
    op.direction = True
    pub.publish(op)
    rospy.sleep(60)
    print("rail end")
    op_end.command = "end"
    op_end.direction = True
    pub_end.publish(op_end)
    rospy.sleep(1)
