'''
This is code for controlling stepper motor with raspberry pi.
Python3 was used, and because of controlling stepper motor with raspberry pi is little bit slow, we don't use this code any more.
But, if stepper motor is changed(faster one, with large max RPM) maybe this code can be used.
'''

from time import sleep
import RPi.GPIO as gpio
import time

 
# PUL = 21
DIR = 20
#ENA = 6
STEP = 21
GO_LEFT =1
GO_RIGHT =0
 
gpio.setmode(gpio.BCM)
 
print("ready\n")
# gpio.setup(PUL, gpio.OUT)
gpio.setup(DIR, gpio.OUT)
#gpio.setup(ENA, gpio.OUT)
gpio.setup(STEP, gpio.OUT)
gpio.output(DIR,GO_RIGHT)
print("start..\n")

gap = 0.0001
two_inch = 41454
cycle = 20

 
# Main body of code
try:
    start1 = time.time()
    gpio.output(DIR,GO_RIGHT)


    ## because it is hard to increase speed of stepper motor at one time, gradually increase the speed of stepper motor
    for x in range(cycle):
        start_temp = time.time()
        for y in range(two_inch):
            gpio.output(STEP,gpio.HIGH)
            sleep(gap)
            gpio.output(STEP,gpio.LOW)
           # sleep(gap)
            if gap > 0.000065:
             gap = gap - 0.000001
        print("time ", x, ": ", time.time() - start_temp)
    print("all time: ", time.time() - start1)


            
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
    
    
finally:
    print("clean up")
    gpio.cleanup()
