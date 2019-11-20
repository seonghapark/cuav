#from cv_bridge import CvBridge, CvBridgeError
from threading import Thread
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure
#from matplotlib.colors import BoundaryNorm
#from matplotlib import animation
#import matplotlib.pyplot as plt
#import matplotlib.colors as colors
#import numpy as np


##### Running Flask(web)
class web_service(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		print('Running Project!')
		global app
		app.run(debug=True)


##### Ros Message management
class ros_service(Thread):
	def __init__(self, plotter):
		global result_time
		global result_data
		global data_num
		global cv_camera_img
		global cv_sar_img

		self.result_time = []
		self.result_data = []
		self.cv_camera_img = []
		self.cv_sar_img = []
		# self.plot = plotter

	def listener(self):
		rospy.init_node('WEB', anonymous=True)
		rospy.Subscriber('Decision,', result, self.data_callback) # 
		print('ros_service: BEFORE spin')
		rospy.spin()
		print('ros_service: AFTER spin')


	def data_callback(self, msg):
		if '카메라':
			self.img_callback(self, msg)
		else if 'sar':
			self.img_callback(self, msg)
		else: ######################################## check from SAR Team
			self.wav_callback(self, data)


	# wav files?? (sar..)
	def wav_callback(self, data):
		print('ros_service: START wav(data_disassembler)')
		self.data_disassembler(data)
		print('ros_service: FINISH wav(data_disassembler)')

	def data_disassembler(self, body):
		print('ros_service: doing disassembler')
		self.data_num = body.num
		print('body num: ', body.num)
		self.result_time = np.fromstring(body.time, dtype=np.float64)
		self.result_data = np.fromstring(body.data, dtype=np.float64)
		self.result_data = np.reshape(self.result_data, (int(len(self.result_time)), int(len(self.result_data)/len(self.result_time))))
       	self.plot.set(self.result_time, self.result_data) 


    # Image files: camera, sar
    # (Reference: https://gist.github.com/rethink-imcmahon/77a1a4d5506258f3dc1f)
	def img_callback(self, msg):
		print('ros_service: START img')
		cv_camera_img = ""
		cv_sar_img = ""
		try:
			cv_camera_img = bridge.imgmsg_to_cv2(msg, "bgr8")
			cv_sar_img = bridge.imgmsg_to_cv2(msg, "bgr8")
		except CvBridgeError, e:
			print('CvBridgeError: ', e)
		else:
			cv.imwrite('camera_img' + self.data_num + '.png', cv_camera_img)
			cv.imwrite('sar_img' + self.data_num + '.png', cv_sar_img)