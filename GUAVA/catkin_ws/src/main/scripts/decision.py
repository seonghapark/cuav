#!/usr/bin/env python3
# -*-coding:utf-8-*-

import rospy
from threading import Thread
from std_msgs.msg import String
from main.msg import operate
from camera.msg import sendframe
from datetime import datetime
from main.msg import realtime
import time

init_finish = False
cycle_finish = False
status = [False, False]


def terminate():
    # log
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format('main', 'decision', str_time, 'decision node will be terminated..')
    print(log)
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
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'SUB', str_time2,
                                             "Get Message From <rail_end> topic : " + data.data)
    pub_log.publish(log_result)
    print(log_result)


def callback_radar(data, args):
    pub_log = args
    rospy.loginfo(rospy.get_caller_id() + " : %s", data.data)
    status[0] = True

    # publish/subscribe log
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'SUB', str_time2,
                                             "Get Message From <result_radar> topic : " + data.data)
    pub_log.publish(log_result)
    print(log_result)


def callback_summary_camera(data, args):
    pub_log = args

    status[1] = True

    # publish/subscribe log
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'SUB', str_time2,
                                             "Get Message From <summary_camera> topic")
    pub_log.publish(log_result)
    print(log_result)


def callback_realtime_camera(data, args):
    pub_log = args[0]
    pub_realtime = args[1]

    # publish/subscriber log
    str_time3 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'SUB', str_time3,
                                             "Get Message From <realtime_camera> topic")
    pub_log.publish(log_result)
    print(log_result)

    # assign values to new message
    realtime_result = realtime()
    realtime_result.object = data.object
    realtime_result.coords = data.coords
    realtime_result.percent = data.percent
    realtime_result.frame = data.frame

    # publish to storage
    pub_realtime.publish(realtime_result)

    # publish/subscriber log
    str_time3 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'PUB', str_time3,
                                             "Send Message to <realtime_result> topic")
    pub_log.publish(log_result)
    print(log_result)



    # publish to web




# transmit information to web node whenever receiving data.

def is_ready(pub_storage, pub_web):
    time.sleep(2)
    print("waiting results...")
    try:
        while status[0] == False or status[1] == False:
            pass
    # if two results are received...
    ### processing results... ###

    # later.. the type is not String type. that will be change to custom message type
    except KeyboardInterrupt:
        pass
    rate = rospy.Rate(10)
    result_message = "done!"
    rospy.loginfo("storage! I'm " + result_message)
    rospy.loginfo("web! I'm " + result_message)

    pub_storage.publish("storage!, I'm " + result_message)
    pub_web.publish("web!, I'm " + result_message)


# rate.sleep()


def decision(pub_log):
    init()

    ############################ init phase ################################

    init_message = operate()
    init_message.command = "init"
    init_message.direction = True

    pub_operate = rospy.Publisher('operate', operate, queue_size=10)
    pub_end = rospy.Publisher('end', operate, queue_size=10)
    # pub_log = rospy.Publisher('logs', String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.loginfo(init_message)
    pub_operate.publish(init_message)

    # publish/subscribe log
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'PUB', str_time2,
                                             "Publsih Message to <operate> topic : " + init_message.command)
    pub_log.publish(log_result)
    print(log_result)
    # rate.sleep()

    # wait signal from railnode
    print("waiting init finished..")
    while init_finish == False:
        pass
    print("start phase..")
    ############################ start phase ################################

    start_message = operate()
    start_message.command = "start"
    start_message.direction = True  # default value.

    rospy.loginfo(start_message)
    pub_operate.publish(start_message)

    # publish/subscribe log
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'PUB', str_time2,
                                             "Publsih Message to <operate> topic : " + start_message.command)
    pub_log.publish(log_result)
    print(log_result)
    # rate.sleep()

    # wait signal from railnode
    print("waiting init finished..")
    while cycle_finish == False:
        pass
    print("end phase..")

    ############################ end phase ################################

    start_message = operate()
    start_message.command = "end"
    start_message.direction = True  # default value.

    rospy.loginfo(start_message)
    pub_end.publish(start_message)

    # publish/subscribe log
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'decision', 'PUB', str_time2,
                                             "Publsih Message to <end> topic : " + start_message.command)
    pub_log.publish(log_result)
    print(log_result)

    rospy.on_shutdown(terminate)


# rate.sleep()


def init():
    rospy.init_node('decision', anonymous=True)
    # log
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format('main', 'decision', str_time, 'decision node is initialized..')
    print(log)
    pub_log.publish(log)

    rospy.Subscriber('result_radar', String, callback_radar, pub_log)
    rospy.Subscriber('summary_camera', sendframe, callback_summary_camera, pub_log)
    rospy.Subscriber('realtime_camera', sendframe, callback_realtime_camera, (pub_log, pub_realtime))
    rospy.Subscriber('rail_end', String, callback_rail_end, pub_log)


if __name__ == '__main__':
    pub_storage = rospy.Publisher('result_storage', String, queue_size=10)
    pub_web = rospy.Publisher('result_web', String, queue_size=10)
    pub_log = rospy.Publisher('logs', String, queue_size=10)
    pub_realtime = rospy.Publisher('realtime_result', realtime, queue_size=10)

    th2 = Thread(target=is_ready, args=(pub_storage, pub_web))
    th2.start()
    decision(pub_log)
    rospy.spin()
    th2.join()
