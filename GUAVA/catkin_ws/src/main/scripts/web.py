#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from threading import Thread
from std_msgs.msg import String
from main.msg import operate
from datetime import datetime
import time

def callback_web(data, args):
    pub_log = args
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'web', 'SUB', str_time2,
                                             "Get Message From <result> topic : ")

    pub_log.publish(log_result)
    print(log_result)


    ### use data ###


def web(pub_log):
    init()

    ### implement web ###

def init():
    rospy.init_node('web',anonymous=True)
    #log
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format('main', 'web', str_time, 'web node is initialized..')
    print(log)
    pub_log.publish(log)

    rospy.Subscriber('result', String, callback_web, pub_log)


if __name__ == '__main__':
    pub_log = rospy.Publisher('logs',String,queue_size=10)

    web(pub_log)
    rospy.spin()