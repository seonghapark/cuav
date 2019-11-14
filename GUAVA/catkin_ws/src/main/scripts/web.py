#!/usr/bin/env python3
#-*-coding:utf-8-*-
import rospy
from threading import Thread
from std_msgs.msg import String
from main.msg import operate
from datetime import datetime
import time
from flask import Flask, render_template, request, Response, url_for, redirect

##############################
# ROS functions
#############################
def callback_web(data, args):
    # write logs
    pub_log = args
    str_time2 = str(datetime.now()).replace(' ', '_')
    log_result = '[{}/{}][{}][{}] {}'.format('main', 'web', 'SUB', str_time2,
                                             "Get Message From <result> topic : ")

    pub_log.publish(log_result)
    print(log_result)


    # load datas
    DecisionValues = DecisionClass(data.coords_camera, data.percent_camera, data.percent_radar, data.image_camera, data.image_radar, data.direction)
    image_camera_name = DecisionValues.image_camera_name
    image_sar_name = DecisionValues.image_sar_name
    camera_accuracy = DecisionValues.percent_camera
    radar_accuracy = DecisionValus.percent_radar

    result = (image_camera_name, image_sar_name, camera_accuracy, radar_accuracy)
    return result


def web(pub_log):
    init()



def init():
    rospy.init_node('web', anonymous=True)
    #log
    str_time = str(datetime.now()).replace(' ', '_')
    log = '[{}/{}][{}] {}'.format('main', 'web', str_time, 'web node is initialized..')
    print(log)
    pub_log.publish(log)

    rospy.Subscriber('final_result', String, callback_web, pub_log)





##############################
# default setting
##############################
app = Flask(__name__)



# default connect
@app.route("/")
def index():
    return render_template('index.html')

            
# click START button(getting images)
@app.route("/getData", methods=['POST'])
def getData():
    if request.method == 'POST':
        ####result = callback_web()
        cameraIMGpath = result[0]
        sarIMGpath = result[1]
        cameraeAccuracy = result[2]
        radarAccuracy = result[3]
        print("Flask running: Deploy Web(post)")
        return render_template('index.html', cameraIMG=cameraIMGpath, sarIMG=sarIMGpath, cameraACCURACY=camera_accuracy, radarACCURACY=radarAccuracy)





##############################
# Running web.py
##############################
if __name__ == '__main__':
    pub_log = rospy.Publisher('logs',String,queue_size=10)

    web(pub_log)
    rospy.spin()
    
    app.run(debug=True)