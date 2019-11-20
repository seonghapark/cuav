#! /usr/bin/env python3

import rospy
import time
from main.msg import operate

print('fake_start')
rospy.init_node("fake_start")
start = rospy.Publisher('operate', operate, queue_size=1)
end = rospy.Publisher('end', operate, queue_size=1)
message = operate()
rate = rospy.Rate(0.2)
#while not rospy.is_shutdown():
rate.sleep()
message.command = 'start'
print("system start")
start.publish(message)
#time.sleep(70)
#message.command = 'end'
#print("system end")
#end.publish(message)
