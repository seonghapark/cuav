# Counter UAV Radar - Fall 2019


Inbae
Kyungyeon 
Haeeun

<br/>
김도진 - <br/>
  My role for this project was to create an object detection model that can detect drone, car, and person. At the beginning, I wrote python code that reads the video or webcam and detects objects that are defined in COCO dataset. I wrote 3 codes, which are codes that detect objects with pre-trained yolov3 and yolov3-tiny models using opencv DNN, Pytorch, and Tensorflow. Compared performance of each codes and concluded that if not using the GPU while inferring, using opencv DNN is the fastest. I ended up using yolov3 and yolov3-tiny because it is much faster than faster rcnn or mask rcnn. <br/><br/>
  
  After figuring out what framework to use, I searched for image datasets to train yolov3. I found about 2600 drone images from github and about 2600 person & car images from Pascal VOC dataset. I converted Pascal VOC dataset labels into YOLO format. While converting to YOLO format, imprecise labels were generated so I looked all images and fixed labels. After dataset was prepared, I used google colab to train custom classes. I used google colab because training process required GPU but I did not have one. Google colab provided free GPUs for 12hours per session. Training dataset took about 18 hours.<br/>
  
  In coming weeks, I will install ros in raspberry pi and upload custom-trained yolo weights, detection codes to the device. I will test how well the model detects objects. If the accuracy is low I will figure out other ways to enhance the performance. Also, I will integrate camera detetion system with ros nodes. If everything is set I will help radar team for analyzing the SAR image using machine learning. I am not familiar with ros so integrating might be difficult, but I will ask other teammates who are familiar with ros to solve the problem.  
<br/>
Below is gif showing how drones are detected using pre-trained yolo drone weight

[Drone-detection](https://i.imgur.com/5UL6AvU.gifv)

Below is repository I am working on for camera detection

[drone_detection Repo](https://github.com/dojinkimm/drone_detection)
  
<br><br><br>

#### Kyeongnam Kim-
 My role in this project is to control drones automatically.  
I'm going to use DJI Phantom 2(Drone) and UgCS(Ground Station Software).
* UgCS: I'm currently researching how to connect laptops-smartphones-DJI Phantom2 while learning how to use UgCS. I'm going to try again because the connection between the laptop and the drone was successful, but the connection between the smartphone and the drone was unsuccessful. Also, I am going to investigate whether I can adjust ground station without my smartphone.
* DJI Phantom2: I'm learning about drone preparation and drone control with Kar Ee. According to Kar Ee, the drone will have a green light if it's calibration in the area where the GPS is caught. Since I have been banned from flying drones from K-Square's conference room, I plan to fly drone from Professor Tony's farm. I'm going to ask Professor Tony that whether I can fly drones on his farm after learning some basic drone control.

<br/><br>
#### Inbae Kang
- My role in this project is the ROS part. ROS is a system that defines the nodes that play each role and defines the topics and messages so that they can communicate with each other smoothly. So far, I have designed the overall design on the ROS of the Counter UAV Project, defined the necessary messages, topics, and nodes, and are implementing each node and message in code.<br/><br>

- In implementing a Decision node that announces the start of a cycle and receives the results, there was a synchronization problem when receiving messages from both nodes, which was solved by threading. I implemented Decision and Storage nodes, but the result message format is not yet confirmed in Camera and Radar, so I used String from std_msgs package. In the case of the Storage node, when the message is received, a file with the current time is created and stored in a subdirectory in the main package. In addition, the basic ROS code of the camera node is implemented to make the camera part work faster.<br/><br>
  
- So far, I have had trouble installing ROS Kinetic on the Raspberry Pi, but it is currently resolved. In addition, I plan to write shell scripts to build an environment for testing and to specify test scenarios and rehearsals. I also plan to write custom messages and materialize the code as the message types for each part become specific.

#### Youngjin  
# Making SAR image from Radar data

We're trying to detect UAV using radar and camera. In this system, radar and camera are used to identify object in surveillance area.

This is Radar team. We receive data from radar, which is moving over the connected rail. Rail starts moving one end of the side and moves to the other end of the side. Velocity of moving rail should be constant. When rail finishes move side to side, one SAR image data is produced. We use this image to classify the object in front of radar. Our goal is classify 4 kinds of object, Human, Car, UAV, and etc.

I took part of analyzing python codes.  Under this paragraph is explaining how codes work, how data are move, how SAR image is generate.

---

# Get Data From Radar (0_get_data.py)

- When 'radar start' signal received, send 'start moving' signal to rail.
- After send signal to rail, radar begins to receive data.
- Stacks data until rail finishes move one side to the other side.
- When rail sends signal of 'finish movement', publish stacked data (BYTE Array).

# Analyze and Parse Raw data (2_analyzer.py)

- Wait until raw data is passed by data receiver(0_get_data.py).
- Parse raw data into two part, sync and data.
- Binary form of data

    ---

    First Byte           | Second Byte

    0b'00SDDDDD' | 0b'110DDDDD'

    ---

    S : Sync, 0 or 1 to distinguish True portion of Data

    D : Data  

    ---

- Receiver module of radar receive produces 10-bit data and divide those data to two bytes.
- Each byte has half of data.
- Combine Two byte and produce one pair of sync and data
- Publish parsed data.

# Process data and make SAR image (make_sar_image.py)

- Wait until parsed data is passed by analyzer(2_analyzer.py).
- make SAR image from parsed data.
    1. Get SAR frame
        - Use sync to separate Frame.
        - There should be long enough period of silence between sync, so we have to set threshold of silence length.
        - After setting minimum silence length, find regions where length between two syncs are over minimum silence length. These regions are where we slice data to get SAR frame.
        - Each region, slice data for get SAR frame. Important thing is use the **second complete positive-valued period** in the region.
        - After slicing data, take Hilbert Transform of each frame.
        - When finishes get SAR frames, subtract mean of all SAR frames from each frames. It gets rid of DC phase component which occurred from transmit-to-receive antenna.
    2. Range Migration Algorithm(RMA)
        - Apply RMA to SAR frames, Produces SAR image.
    3. Plot image
        - Plot image to user.
        - We use this image to classify objects(UAV, Car, Human, etc.), So publish image data to classifier.

# Classify object using SAR image

- Probability of using CNN or RNN to classify objects from image data.

---

## Things to do

- I succeed transferring data between nodes in ROS.
- But SAR image doesn't come out, I think this is because difference of radar between MIT's and ours. I need to adjust parameters such as sample rate, radio frequency, pulse period. After adjusting these parameters, I wish SAR image comes out properly.

p.s. I tried to study Range Migration Algorithm, but it's bit too hard for me.. haha..

---


**Haeeun** <br/>

I took part of test radar. 
Before the test, We try to understand and construct the node of radar. Then I changed `get_data.py` to ROS. We performed field test to check the radar and we could check some facts through it. The results are under the documents. 
Now I'm changing `draw.py` to ROS for checking figure of raw data from radar.

### Indoor
![image](https://user-images.githubusercontent.com/44107947/66231980-d182f380-e6b5-11e9-808c-be64434d26ab.png)
![image](https://user-images.githubusercontent.com/44107947/66231988-d8116b00-e6b5-11e9-8572-15e8a708d1ba.png)
- It was tested in conference room
- A person moved back and forth with an iron plate(about 30x30).

### Outdoor

**1. Nothing**
![image](https://user-images.githubusercontent.com/44107947/66232011-e5c6f080-e6b5-11e9-9f76-61325392820f.png)

- We tested at empty place between K-SW Square and Anvil.

**2. Moving back and forth**
![image](https://user-images.githubusercontent.com/44107947/66232031-ef505880-e6b5-11e9-9d61-a481e8b915c3.png)
![image](https://user-images.githubusercontent.com/44107947/66232035-f5463980-e6b5-11e9-9632-be1b4356e5e3.png)

- It is assumed that it can recognize things in about 12m.
- A person moved back and forth with an iron plate(about 30x30).

**3. Change antenna height (around 120cm)**
![image](https://user-images.githubusercontent.com/44107947/66232048-fd05de00-e6b5-11e9-8a80-5f24dd806123.png)

- It was measured holding by hand and the height is about 120cm.
- We can check that noise was reduced than when the radar was on the table.
- It is not sure that the reason is the table or height of the radar, but we requested that a rail will be over 120cm.

**4. Moving back and forth in 120cm**
![image](https://user-images.githubusercontent.com/44107947/66232059-03945580-e6b6-11e9-9b95-439c666f6e94.png)


<br/>

**Kyungyeon Park**

I was in charge of making rail. There are not a lot of components in KSQ, so I have to buy all the components. But the components are late and the progress is being delayed. First, I ordered the motor and the motor driver and assembled it with the Raspberry Pi. Next, I ordered the power adapter and the ball screw and connected it with the motor, the motor driver and the Raspberry Pi. I tried to use the robot profile in KSQ as a rail support, but it didn't match with the ball screw so I ordered a new 30mm x 60mm profile. I expect new items to arrive by the end of the fall break. The supporter on which the radar will be placed will be printed out by the 3D printer, fixed in the profile with bearings and screwed in the nut housing (ball screw nut) (see figure below).

<img src="https://i.ibb.co/g4NmHqD/rail.jpg" width="50%">

The parts came slowly, so in advance, I calculated some data about the step that stepper motor needs to go one round and the step that stepper needs to go 1 inch. I've been experimenting with the python code to see whether the motor is running exactly one round, and it seems to run one round. But I think I need to think about how to prove this exactly. The calculation is correct, but there seems to be a little error due to friction.

Next, I installed ROS on the raspberry pi of the rail to be used to control the stepper motor. Previously I used Raspbian Buster as my OS for Raspberry Pi, but when I installed ROS Kinetic on Raspbian buster, I kept getting an error. So I used Raspbian Jessie for my OS and I could successfully install ROS on the Raspberry Pi. Also, I installed the ROS on the Raspberry Pi of the camera side.

The process of connecting wires and making rails is detailed in the [Making rail Wiki](https://github.com/seonghapark/cuav/wiki/Making-Rail). I would appreciate it for your reference.
