#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String
from datetime import datetime

#log file generate
directory = '/home/project/cuav/GUAVA/catkin_ws/src/radar/logs/rail/'
str_time = str(datetime.now()).replace(' ', '_')
file_name = directory + str_time + '_' + 'radar' + '_' + 'rail' + '.log'
file_log = open(file_name, 'w')




def callback_operate(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	str_time2 = str(datetime.now()).replace(' ', '_')
	log_result = '[{}/{}][{}][{}] {}'.format('radar','rail','SUB',str_time2,"Get Message From <operate> topic : "+data.data)
	print(log_result, file=file_log)
	print(log_result)

	#if(data.dir == 0):
		#0방향 움직이는 코드.
	#else:
		#1방향 움직이는 코드.

	#움직인 후
	pub = rospy.Publisher('terminate', String, queue_size=10)
	terminate_message = "Moving Rail is complete."
	rospy.loginfo(terminate_message)
	pub.publish(terminate_message)

	#publish/subscribe log
	str_time2 = str(datetime.now()).replace(' ','_')
	log_result ='[{}/{}][{}][{}] {}'.format('radar','rail','PUB',str_time2,"Publsih Message to <terminate> topic : "+terminate_message)
	print(log_result,file=file_log)
	print(log_result)

	

def rail():
	
	#log
	str_time = str(datetime.now()).replace(' ', '_')
	log ='[{}/{}][{}] {}'.format('main','storage',str_time,'storage node is initialized..')
	print(log)
	print(log,file=file_log)

	rospy.init_node('rail', anonymous=True)
	rospy.Subscriber('operate', String, callback_operate)
	rospy.spin()

if __name__ == '__main__':
	rail()

	

