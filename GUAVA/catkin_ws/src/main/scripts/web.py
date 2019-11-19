#!/usr/bin/env python3
#-*-coding:utf-8-*-
import rospy
from threading import Thread
from std_msgs.msg import String
from main.msg import result_web
from flask import Flask, render_template, request, Response, url_for, redirect
from main_log import log_generator

#############################
# Global variables
#############################
result = ()
app = Flask(__name__, static_folder='/home/project/cuav/GUAVA/catkin_ws/src/main/storage/')


#############################
# ROS functions
#############################
class ROSWeb(Thread):
    @staticmethod
    def web_callback(data, args):
        # write logs
        global result
        pub_log = args

        # log
        log = log_generator('web', "result", 'sub')
        pub_log.publish(log)

        # load data
        image_camera_name = data.image_camera
        camera_accuracy = round(data.percent_camera, 4) * 100
        print(camera_accuracy)
        print(round(data.percent_camera, 4) * 100)
        print((round(data.percent_camera*100, 2)))
        # camera_coords = data.coords_camera
        # camera_direction = data.direction
        # image_sar_name = data.image_radar
        # radar_accuracy = data.percent_radar

        #result = (image_camera_name, camera_accuracy, image_sar_name, radar_accuracy)
        result = (image_camera_name, camera_accuracy)

    def listener(self):
        rospy.init_node('web', anonymous=True)

        pub_log = rospy.Publisher('logs', String, queue_size=10)

        # log
        log = log_generator('web', 'web node is initialized..')
        pub_log.publish(log)

        rospy.Subscriber('result_web', result_web, self.web_callback, pub_log)
        rospy.spin()


##############################
# Flask functions
##############################
class WebService(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global app
        app.run(host='192.168.2.128')


# default connect
@app.route("/")
def index():
    return render_template('index.html')

           
# click START button(getting images)
@app.route("/getData", methods=['POST'])
def getData():
    if request.method == 'POST':
        global result
        ####result = callback_web()

        cameraIMGpath = result[0]
        cameraAccuracy = result[1]
        # sarIMGpath = result[2]
        # radarAccuracy = result[3]
        #return render_template('index.html', cameraIMG=cameraIMGpath, sarIMG=sarIMGpath, cameraACCURACY=camera_accuracy, radarACCURACY=radarAccuracy)
        return render_template('index.html', cameraIMG=cameraIMGpath, cameraACCURACY=cameraAccuracy)


##############################
# Running web.py
##############################
if __name__ == '__main__':
    w = WebService()
    w.start()
    r = ROSWeb()
    r.listener()

