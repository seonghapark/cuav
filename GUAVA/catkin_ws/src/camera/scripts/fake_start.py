#! /usr/bin/env python3

import rospy
from main.msg import operate


print('fake_start')
rospy.init_node("fake_decision")
pub = rospy.Publisher('operate', operate, queue_size=3)
rate = rospy.Rate(5)
op = operate()
op.command = "init"
op.direction = True
print("system start")
while not rospy.is_shutdown():
    rospy.sleep(1)
    pub.publish(op)
    print('init sended')
    rospy.sleep(6000)
