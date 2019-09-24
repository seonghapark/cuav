#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String #std_msgs/String 메시지 타입을 사용할 수 있도록.

def prac1():
	#chatter topic에 publish하는 노드를 정의 메시지 타입은 String(std_msg안에)
	pub = rospy.Publisher('chatter', String, queue_size=10) 
	#Master 노드에게 노드를 알려주도록 initialize, 이름에는 /포함되면 안됨.
	rospy.init_node('prac1', anonymous=True)
	#sleep을 도와주도록하는 rate 객체 생성. 1초에 10번의 loop를 돌도록 설정.
	rate = rospy.Rate(10) #10hz
	while not rospy.is_shutdown(): #끝날 때 까지 진행하는데
		hello_str = "hello World! %s" % rospy.get_time()
		#메시지를 스크린에 프린트, 노드의 로그파일에 기록, rosout에도 기록
		rospy.loginfo(hello_str)
		
		pub.publish(hello_str)
		rate.sleep()
if __name__ == '__main__':
	try:
		prac1()
	except rospy.ROSInterruptException:
		pass

