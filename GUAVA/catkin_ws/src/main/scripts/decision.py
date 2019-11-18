#!/usr/bin/env python3
# -*-coding:utf-8-*-

import rospy
from threading import Thread
import time
from camera.msg import sendframe, sendsummary
from std_msgs.msg import String
from main.msg import operate, realtime, result
from DecisionClass import DecisionClass
from main_log import log_generator

DecisionValues = DecisionClass()


init_finish = False
cycle_finish = False
status = [False, False]


def terminate():
    # log
    log = log_generator('decision', 'Decision node will be terminated..', 'pub')
    pub_log.publish(log)

    rospy.signal_shutdown("decision node terminated.")


def callback_rail_end(data, args):
    pub_log = args
    global init_finish
    global cycle_finish
    rospy.loginfo(rospy.get_caller_id() + " : %s", data.data)
    if data.data == "init_finish":
        init_finish = True
    if data.data == "cycle_finish":
        cycle_finish = True

    # publish/subscribe log
    log = log_generator('decision', "Receive Message From <rail_end> topic : " + data.data, 'sub')
    pub_log.publish(log)


def callback_radar(data, args):
    pub_log = args
    rospy.loginfo(rospy.get_caller_id() + " : %s", data.data)
    status[0] = True

    # publish/subscribe log
    log = log_generator('decision', "Receive Message From <result_radar> topic", 'sub')
    pub_log.publish(log)


    DecisionValues.image_radar = data.sar
    DecisionValues.percent_radar = data.percent


def callback_summary_camera(data, args):
    pub_log = args

    status[1] = True

    # publish/subscribe log
    log = log_generator('decision', "Receive Message From <summary_camera> topic", 'sub')
    pub_log.publish(log)

    # update decision values
    DecisionValues.image_camera = data.frame
    DecisionValues.percent_camera = data.percent
    DecisionValues.direction = data.direction


def callback_realtime_camera(data, args):
    pub_log = args[0]
    pub_realtime = args[1]

    # publish/subscriber log
    log = log_generator('decision', "Receive Message From <realtime_camera> topic", 'sub')
    pub_log.publish(log)

    # assign values to new message
    realtime_result = realtime()
    realtime_result.coords = data.coords
    realtime_result.percent = data.percent
    realtime_result.frame = data.frame

    # publish to storage
    pub_realtime.publish(realtime_result)

    # publish/subscriber log
    log = log_generator('decision', "Send Message to <realtime_result> topic", 'pub')
    pub_log.publish(log)

    # publish to web


# transmit information to web node whenever receiving data.
def is_ready(pub_decision_result, pub_log):
    time.sleep(2)
    log = log_generator('decision', 'waiting results from radar and camera')
    pub_log.publish(log)
    try:
        while status[0] == False or status[1] == False:
            pass

    # later.. the type is not String type. that will be changed to custom message type
    except KeyboardInterrupt:
        pass
    rate = rospy.Rate(10)

    # if two results are received...
    log = log_generator('decision', 'All results are received. It will be transferred to storage node')
    pub_log(log)

    # message generation
    result_message = DecisionClass.generate_storage_message()

    # publish to storage node
    pub_decision_result.publish(result_message)

    # publish/subscriber log
    log = log_generator('decision', "Send Message to <result> topic", 'pub')
    pub_log.publish(log)


def decision(pub_log):
    init()

    ############################ init phase ################################

    log = log_generator('decision', ' ** init phase **')
    pub_log.publish(pub_log)

    # generate message for init
    init_message = operate()
    init_message.command = "init"
    init_message.direction = True

    pub_operate = rospy.Publisher('operate', operate, queue_size=10)
    pub_end = rospy.Publisher('end', operate, queue_size=10)
    # pub_log = rospy.Publisher('logs', String, queue_size=10)
    rate = rospy.Rate(10)

    pub_operate.publish(init_message)

    # publish/subscribe log
    log = log_generator('decision', "Send Message to <operate> topic : " + init_message.command, 'pub')
    pub_log.publish(log)

    # wait signal from railnode
    log = log_generator('decision', "waiting init finished..")
    pub_log(log)


    while init_finish == False:
        pass

    ############################ start phase ################################

    log = log_generator('decision', ' ** start phase **')
    pub_log.publish(pub_log)

    start_message = operate()
    start_message.command = "start"
    start_message.direction = True  # default value.

    rospy.loginfo(start_message)
    pub_operate.publish(start_message)

    # publish/subscribe log
    log = log_generator('decision', "Send Message to <operate> topic : " + start_message.command, 'pub')
    pub_log.publish(log)

    # wait signal from railnode
    log = log_generator('decision', "waiting cycle finished..")
    pub_log(log)

    while not cycle_finish == False:
        pass


    ############################ end phase ################################

    log = log_generator('decision', ' ** end phase **')
    pub_log.publish(pub_log)

    start_message = operate()
    start_message.command = "end"
    start_message.direction = True  # default value.

    rospy.loginfo(start_message)
    pub_end.publish(start_message)

    # publish/subscribe log
    log = log_generator('decision', "Send Message to <end> topic : " + start_message.command, 'pub')
    pub_log.publish(log)

    rospy.on_shutdown(terminate)



def init():
    rospy.init_node('decision', anonymous=True)

    # log
    log = log_generator('decision', 'Decision node is initialized..')
    pub_log.publish(log)

    rospy.Subscriber('result_radar', String, callback_radar, pub_log)
    rospy.Subscriber('summary_camera', sendsummary, callback_summary_camera, pub_log)
    rospy.Subscriber('realtime_camera', sendframe, callback_realtime_camera, (pub_log, pub_realtime))
    rospy.Subscriber('rail_end', String, callback_rail_end, pub_log)


if __name__ == '__main__':
    pub_decision_result = rospy.Publisher('final_result', result, queue_size=10)
    pub_log = rospy.Publisher('logs', String, queue_size=10)
    pub_realtime = rospy.Publisher('realtime_result', realtime, queue_size=10)

    th2 = Thread(target=is_ready, args=(pub_decision_result, pub_log))
    th2.start()
    decision(pub_log)
    rospy.spin()
    th2.join()
