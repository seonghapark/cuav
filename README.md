# Counter UAV Radar - Fall 2019

Youngjin
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

<br/>
#### Inbae Kang - 
- My role in this project is the ROS part. ROS is a system that defines the nodes that play each role and defines the topics and messages so that they can communicate with each other smoothly. So far, I have designed the overall design on the ROS of the Counter UAV Project, defined the necessary messages, topics, and nodes, and are implementing each node and message in code.

  In implementing a Decision node that announces the start of a cycle and receives the results, there was a synchronization problem when receiving messages from both nodes, which was solved by threading. I implemented Decision and Storage nodes, but the result message format is not yet confirmed in Camera and Radar, so I used String from std_msgs package. In the case of the Storage node, when the message is received, a file with the current time is created and stored in a subdirectory in the main package. In addition, the basic ROS code of the camera node is implemented to make the camera part work faster.
  
So far, I have had trouble installing ROS Kinetic on the Raspberry Pi, but it is currently resolved. In addition, I plan to write shell scripts to build an environment for testing and to specify test scenarios and rehearsals. I also plan to write custom messages and materialize the code as the message types for each part become specific.

<br/><br/><br/>
