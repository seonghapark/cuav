#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String
from datetime import datetime

#log file generation
directory = '/home/project/cuav/GUAVA/catkin_ws/src/main/logs/'
str_time = str(datetime.now()).replace(' ', '_')
file_name = directory + str_time + '.log'
file_log = open(file_name, 'w')

def callback_logs(data):
	if str(data.data) == "end":
		str_time = str(datetime.now()).replace(' ', '_')
		log = '[{}/{}][{}] {}'.format('main', 'log', str_time, 'end signal received..')
		print(log)
		print(log, file=file_log)
		file_log.close()
		rospy.signal_shutdown("log node terminated.")
	else:
		#rospy.loginfo(rospy.get_caller_id() + " : %s", data.data)
		print(data.data)
		print(data.data, file=file_log)


def log():
	while not rospy.is_shutdown() :
		str_time = str(datetime.now()).replace(' ', '_')
		log ='[{}/{}][{}] {}'.format('main','log',str_time,'log node is initialized..')
		print(log)
		print(log,file=file_log)

		rospy.init_node('log', anonymous=True)
		rospy.Subscriber('logs', String, callback_logs)
		rospy.spin()

if __name__ == '__main__':
	log()

