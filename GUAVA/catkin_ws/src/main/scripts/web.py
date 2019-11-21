#!/usr/bin/env python3
#-*-coding:utf-8-*-
import rospy
from threading import Thread
from std_msgs.msg import String
from main.msg import result_web
from flask import Flask, render_template, Response, redirect, url_for, request, stream_with_context
from main_log import log_generator

#############################
# Global variables
#############################
result = ()
app = Flask(__name__, static_folder='/home/project/cuav/GUAVA/catkin_ws/src/main/storage')

#############################
# ROS functions
#############################
class ROSWeb(Thread):
    @staticmethod
    def web_callback(data, args):
        # write logs
        global result, app
        pub_log = args

        # log
        log = log_generator('web', "result", 'sub')
        pub_log.publish(log)

        # load data
        realtime_camera_image = ""
        realtime_camera_accuracy = 0.0
        image_camera_name = ""
        image_camera_accuracy = 0.0
        # camera_coords = data.coords_camera
        # camera_direction = data.direction
        image_sar_name = data.image_radar
        # radar_accuracy = round(data.percent_radar * 100, 2)

        if image_sar_name == "": # realtime camera image
            realtime_camera_image = data.image_camera
            realtime_camera_accuracy = round(data.percent_camera * 100, 2)
        else:
            image_camera_name = data.image_camera
            image_camera_accuracy = round(data.percent_camera * 100, 2)

        print(realtime_camera_image, realtime_camera_accuracy, "WEB NODE RESULT")

        #result = (image_camera_name, camera_accuracy, realtime_camera_image, realtime_camera_accuracy, image_sar_name, radar_accuracy)
        result = (image_camera_name, image_camera_accuracy, realtime_camera_image, realtime_camera_accuracy)

        with app.app_context():
            context = {'realIMG': result[0], 'realACCURACY': result[1]}
            return render_template("index.html", **context)
            #return Response(stream_with_context(generate()))

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
        # app.run(host='192.168.2.128')
        socketio.run(app, host='192.168.2.128')

# default connect
@app.route("/")
def index():
    # return render_template('index.html')
    return render_template('index.html', async_mode=socketio.async_mode)


# click START button(getting images)
@app.route("/getData", methods=['POST'])
def getData():
    if request.method == 'POST':
        global result
        ####result = callback_web()

        cameraIMGpath = result[0]
        cameraAccuracy = result[1]
        realtimeCameraIMG = result[2]
        realtimeCameraAccuracy = result[3]
        # sarIMGpath = result[2]
        # radarAccuracy = result[3]
        #return render_template('index.html', cameraIMG=cameraIMGpath, sarIMG=sarIMGpath, cameraACCURACY=camera_accuracy, radarACCURACY=radarAccuracy)

        if realtimeCameraIMG != "":
            return render_template("index.html", realIMG=realtimeCameraIMG, realACCURACY=realtimeCameraAccuracy)
        else:
            return render_template('index.html', cameraIMG=cameraIMGpath, cameraACCURACY=cameraAccuracy, realIMG=realtimeCameraIMG, realACCURACY=realtimeCameraAccuracy)


##############################
# Running web.py
##############################
if __name__ == '__main__':
    w = WebService()
    w.start()
    r = ROSWeb()
    r.listener()

