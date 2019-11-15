#!/usr/bin/env python3

from threading import Thread
import io

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import animation

import numpy as np
import time
from datetime import datetime
import queue

import rospy
from radar.msg import realtime
from std_msgs.msg import String

PACKAGE_NAME = 'radar'
NODE_NAME = 'plotter'
result_time = []
result_data = []
data_num = 0
q_result_data = queue.Queue()
q_result_time = queue.Queue()

rospy.init_node('plotter', anonymous=True)
log = rospy.Publisher('logs', String, queue_size=100)


class ros_communication():
    def __init__(self, plotter):
        global result_time
        global result_data
        global data_num
        self.result_time = []
        self.result_data = []
        #self.data_num = 0
        self.plot = plotter

    def data_disassembler(self, data):
        self.result_time = np.fromstring(data.sync, dtype=np.float64)
        self.result_data = np.fromstring(data.data, dtype=np.float64)
        self.result_data = np.reshape(self.result_data, (int(len(self.result_time)), int(len(self.result_data)/len(self.result_time))))
        self.plot.set(self.result_time, self.result_data)

    def callback(self, data):
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, 'SUB', str_time, 'Subscribe from realtime_wav')
        log.publish(log_text)
        print(log_text)
        self.data_disassembler(data)


class colorgraph_handler():
    def __init__(self):
        #Thread.__init__(self)
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, 'Initialize plotter')
        log.publish(log_text)
        print(log_text)

        ## constants for frame
        self.n = int(5862/50)  # Samples per a ramp up-time
        # self.n = int(5512/50)
        #self.zpad = 8 * (self.n / 2)  # the number of data in 0.08 seconds?
        self.zpad = 440
        # self.lfm = [2260E6, 2590E6]  # Radar frequency sweep range
        self.lfm = [2400E6, 2500E6]
        self.max_detect = 3E8/(2*(self.lfm[1]-self.lfm[0]))*self.n/2 # Max detection distance according to the radar frequency
        self.set_t = 10 #int(sys.argv[1])  # Frame length on x axis
        # self.set_t = 25  # Frame length on x axis --> 25 seconds

        ## variables for incoming data
        self.y = np.linspace(0,self.max_detect, int(self.zpad/2))
        #self.y = [220, ]
        self.data_tlen = 0
        self.data_t = np.zeros((50))
        self.data_val = np.zeros((50, self.y.shape[0]))

        self.q_result_data = queue.Queue()
        self.q_result_time = queue.Queue()
        self.previous = 0

        ## constants to plot animation, initialize animate function
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.xlabel = plt.xlabel('Time(s)')
        self.ylabel = plt.ylabel('Distance(m)')
        self.ylim = plt.ylim(0, self.max_detect)
        #self.ylim = plt.ylim(0, 1)  ## For bottom noise
        self.cmap = plt.get_cmap('jet')
        self.norm = colors.BoundaryNorm([i for i in range(-80, 1)], ncolors=self.cmap.N, clip=True)
        self.pcolormesh = plt.pcolormesh(self.data_t, self.y, self.data_val.T, norm=self.norm, cmap=self.cmap)
        self.colorbar = plt.colorbar()
        self.colorlabel = self.colorbar.set_label('Intensity (dB)')

    def get_fig(self):
        return self.fig

    def set(self, result_time, result_data):
        print('set')
        if self.previous != result_time.item(0):
            self.previous = result_time.item(0)
            self.q_result_time.put(result_time)
            self.q_result_data.put(result_data)

    def get(self):
        if not self.q_result_time.empty():
            self.data_t = self.q_result_time.get()
            self.data_val = self.q_result_data.get()
            self.data_tlen = len(self.data_t)

    def animate(self, time):
        self.get()
        time = time+1

        if time > self.set_t:
            lim = self.ax.set_xlim(time - self.set_t, time)
        else:
            # makes it look ok when the animation loops
            lim = self.ax.set_xlim(0, self.set_t)

        plt.pcolormesh(self.data_t, self.y, np.swapaxes(self.data_val[:self.data_tlen], 0, 1), norm=self.norm, cmap=self.cmap)
        return self.ax

    def draw_graph(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000, blit=False)
        plt.show()


if __name__ == '__main__':
    plot = colorgraph_handler()
    ros = ros_communication(plot)
    print('before start')
    rospy.Subscriber('realtime_wav', realtime, ros.callback)

    try:
        while (True):
            # print('main while(True)')
            if plot.q_result_time.empty():
                # print('queue is empty')
                time.sleep(1)
            else:
                # print('queue is not empty')
                break
        plot.draw_graph()
    except(KeyboardInterrupt, Exception) as ex:
        print(ex)
    finally:
        str_time = str(datetime.now()).replace(' ', '_')
        log_text = '[{}/{}][{}] {}'.format(PACKAGE_NAME, NODE_NAME, str_time, 'Clase All')
        log.publish(log_text)
        print(log_text)

    rospy.spin()
