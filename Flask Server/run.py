# -*- coding: utf-8 -*-
import os, io, random, time, queue, sys#, rospy, pika, argparse
from flask import Flask, render_template, request, Response, url_for, redirect
# from ros_counteruav.msg import result, objectinfo
# from sensor_msgs.msg import Image
# from src import flask_code
# import random

####################################
# default variables
####################################
app = Flask(__name__)

result_time = []
result_data = []
data_num = 0
q_result_camera = queue.Queue()
q_result_wav = queue.Queue()
q_result_sar = queue.Queue()
q_result_time = queue.Queue()
final_object = ""
final_time = 0


########################################################
# running Server and manage datas
########################################################

@app.route("/")
def index():
	return render_template('index.html')
        	

@app.route("/getData", methods=['POST'])
def getData():
	if request.method == 'POST':
		global data_num
		droneAccuracy = random.randint(1, 100)
		cameraIMGpath = "img/camera_test" + str(data_num) + ".png"
		sarIMGpath = "img/sar_test" + str(data_num) + ".png"
		data_num += 1
		print("Flask running: Deploy Web(post)")
		return render_template('index.html', camera=cameraIMGpath, sar=sarIMGpath, accuracy=droneAccuracy)


if __name__ == '__main__':
	app.run(debug=True)
		# web = web_service()
	#	plot = colorgraph_handler()
	#	ros = ros_service(plot)

		# web.start()
	#	plot.start()
	#	ros.listener()
	#except KeyboardInterrupt:
	#	print("Shut down: keyboard interruption")