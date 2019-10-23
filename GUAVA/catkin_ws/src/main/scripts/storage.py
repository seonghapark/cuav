#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import String
from datetime import datetime
# from main.msg import result

#log file generate
directory = '/home/project/cuav/GUAVA/catkin_ws/src/main/logs/storage/'
str_time = str(datetime.now()).replace(' ','_')
file_name = directory + str_time + '_' + 'main' + '_' + 'storage' + '.log'	
file_log = open(file_name,'w')


def callback_result(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	#publish/subscribe log
	str_time2 = str(datetime.now()).replace(' ','_')
	log_result ='[{}/{}][{}][{}] {}'.format('main','storage','SUB',str_time2,"Get Message From <result> topic : "+data.data)
	print(log_result,file=file_log)
	print(log_result)
	
	# assign the value from parameter(message) to local variable #
	#							     #
	# class = data.class					     #
	# img = data.img					     #
	# ....							     #
	##############################################################

	# make file for backup
	
	now = datetime.now() # current time for filename
	f = open('/home/project/cuav/GUAVA/catkin_ws/src/main/storage/'+str(now)+'.dat','w')
	test_str = ["for test", "teeeeest"]
	test_str.append(data.data)
	f.write('\n'.join(test_str))
	f.close()

def storage():

	#log
	str_time = str(datetime.now()).replace(' ','_')
	log ='[{}/{}][{}] {}'.format('main','storage',str_time,'storage node is initialized..')
	print(log)
	print(log,file=file_log)

	rospy.init_node('storage', anonymous=True)
	rospy.Subscriber('result', String, callback_result)
	rospy.spin()

if __name__ == '__main__':
	storage()
