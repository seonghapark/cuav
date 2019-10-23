#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from threading import Thread
from std_msgs.msg import String
from main.msg import start
from datetime import datetime

status = [False, False]

#log file generate
directory = '/home/project/cuav/GUAVA/catkin_ws/src/main/logs/decision/'
str_time = str(datetime.now()).replace(' ','_')
file_name = directory + str_time + '_' + 'main' + '_' + 'decision' + '.log'
file_log = open(file_name,'w')


def callback_radar(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	status[0] = True
        
	#publish/subscribe log
	str_time2 = str(datetime.now()).replace(' ','_')
	log_result ='[{}/{}][{}][{}] {}'.format('main','decision','SUB',str_time2,"Get Message From <result_radar> topic : "+data.data)
	print(log_result,file=file_log)
	print(log_result)

def callback_summary_camera(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	status[1] = True

	#publish/subscribe log
	str_time2 = str(datetime.now()).replace(' ','_')
	log_result ='[{}/{}][{}][{}] {}'.format('main','decision','SUB',str_time2,"Get Message From <summary_camera> topic : "+data.data)
	print(log_result,file=file_log)
	print(log_result)

def callback_realtime_camera(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	
	print(log_result,file=file_log)
	#publish/subscriber log
	str_time3 = str(datetime.now()).replace(' ', '_')
	log_result ='[{}/{}][{}][{}] {}'.format('main','decision','SUB',str_time2,"Get Message From <realtime_camera> topic : "+data.data)
	print(log_result,file=file_log)
	print(log_result)

	#transmit information to web node whenever receiving data.

def is_ready(pub_storage, pub_web):
	i = 0
	try:
		while status[0] == False or status[1] == False:
			if i%8000000==0:
				print("waiting results...")
			i += 1
		#if two results are received...
	
		### processing results... ###

		#in later.. the type is not String type. that will be change to custom message type
	except KeyboardInterrupt:
		pass
	rate = rospy.Rate(10)
	result_message = "done!"
	rospy.loginfo("storage! I'm " + result_message)
	rospy.loginfo("web! I'm " + result_message)
	
	pub_storage.publish("storage!, I'm " + result_message)
	pub_web.publish("web!, I'm " + result_message)
	rate.sleep()
	

def decision():

	#log
	str_time = str(datetime.now()).replace(' ','_')
	log ='[{}/{}][{}] {}'.format('main','storage',str_time,'decision node is initialized..')
	print(log)
	print(log,file=file_log)	

	pub = rospy.Publisher('start', start, queue_size=10)
	rospy.init_node('decision', anonymous=True)
	rate = rospy.Rate(10)
	#while not rospy.is_shutdown():
	start_message = "Let's get it! current time : %s" % rospy.get_time()
	rospy.loginfo(start_message)
	pub.publish(start_message)
	
	#publish/subscribe log
	str_time2 = str(datetime.now()).replace(' ','_')
	log_result ='[{}/{}][{}][{}] {}'.format('main','storage','PUB',str_time2,"Publsih Message to <result> topic : "+start_message)
	print(log_result,file=file_log)
	print(log_result)
	rate.sleep()

def decision_subscriber():
	rospy.Subscriber('result_radar', String, callback_radar)
	rospy.Subscriber('summary_camera', String, callback_summary_camera)
	rospy.Subscriber('realtime_camera', String, callback_realtime_camera)
	rospy.spin()

if __name__ == '__main__':
	
	pub_storage = rospy.Publisher('result_storage', String, queue_size=10)
	pub_web = rospy.Publisher('result_web', String, queue_size=10)
	
	th2 = Thread(target=is_ready,args=(pub_storage,pub_web))

	decision()
	th2.start()
	decision_subscriber()
	th2.join()

	file_log.close()

	
	
