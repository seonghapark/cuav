# Counter UAV Radar - Fall 2019


Inbae
Kyungyeon 
Haeeun

<br/>
김도진 - <br/>



My role for this project was to create an object detection model that can detect drone, car, and person. At the beginning, I wrote python code that reads the video or webcam and detects objects that are defined in COCO dataset. I used the video downloaded from youtube [DJI PHANTOM 4 RTK – A Game Changer for Construction Surveying](https://www.youtube.com/watch?v=tAuF5aZi1ic). The video was too long, I only maintained video frames that contain drones and removed others. COCO dataset has 80 object categories such as person, car, bus and etc. Categories that are in COCO dataset can be found in this site: [COCO labels](https://github.com/pjreddie/darknet/blob/master/data/coco.names). The purpose of running the code was simply to check whether the code loads yolo weight well and detects objects that are in 80 category.

I wrote 3 codes, which are codes that detect objects with pre-trained yolov3 and yolov3-tiny models using opencv DNN, Pytorch, and Tensorflow. I used both Yolov3 and Yolov3-tiny models, loaded these models in opencv DNN, Pytorch, and Tensorflow to do object detection. I referred to [Object Detection Comparison](https://medium.com/@jonathan_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359) when choosing which model to use. The performance of each models are well described in this article. I used pre-defined network, yolov3 has 75 convolutional layers and yolov3-tiny has 15 layers. Compared performance of each codes and concluded that if not using the GPU while inferring, using opencv DNN is the fastest. I chose yolov3 because it is one of the fastest object detection model. Even though overall accuracy is worse than faster-rcnn, when detecting large objects it performs similarly. I ended up using yolov3 and yolov3-tiny because it is much faster than faster rcnn or mask rcnn. I chose yolov3 because it is one of the fastest object detection model. Even though overall accuracy is worse than faster-rcnn, when detecting large objects it performs similarly. Faster RCNN looks the complete image and predicts objects with region proposals. On the other hand, Yolo does not look at the complete image. It divides the image into n*n grids (the bigger n is accuracy increases but slows down). In grids it takes bounding boxes and the network outputs class probability for the bounding box. This step differentiates two models. Since yolo does not look for the object in the complete image it is faster. <br/><br/>
  
Thus, I concluded to use opencv DNN and yolov3 for camera detection. I found about 2600 drone images from [Github-drone-images](https://github.com/chuanenlin/drone-net) and about 2600 person & car images from Pascal VOC dataset. COCO datasets were extremely large (about 20GB), so I searched for smaller datasets that are already labelled. This is because labelling thousands of images by myself would take a very long time. Pascal VOC dataset was not very large and it was already labelled, so I decided to use it. One problem was that this dataset had different label format from YOLO. Therefore, I used [convert2Yolo](https://github.com/ssaru/convert2Yolo) github repository to convert Pascal VOC dataset labels into YOLO format.  Pascal VOC labels contained 20 categories, but I needed only person and car. Thus, I after converting to YOLO format I looked for images that did not contain either person or car and removed those. Another problem was that the position of the object in the image was described in floating number but only 3 digits were displayed after decimal point(ex. 0 0.712 0.464 0.352 0.271). When I opened the image using the github repository [labelImg](https://github.com/tzutalin/labelImg), I found out that position of boxes were quite imprecise due to the problem I mentioned. I looked over all images to correct the position.<br/><br/>

After dataset was prepared, I used google colab to train custom classes. I used google colab because training process takes a long time and the time can be diminished using GPU. Image processing requires a lot of computation and GPU is faster than CPU when doing computation (referred to article [GPU vs CPU](https://medium.com/@shachishah.ce/do-we-really-need-gpu-for-deep-learning-47042c02efe2)). This is the reason for choosing google colab instead trying to do training in my computer's CPU. I set the learnig rate to 0.001 and trained for 6000 batches, 64 images each for a batch. It took about 3 hours to train 1000 batches, since I set to 6000 batches the total training time took 18 hours. Google colab provides free GPU for 12 hours per session. Thus, I saved weight every 1000 batches, so when the session expired I again began from previously saved weight.<br/>
  
After a meeting, I re-trained a model so that it could detect only drones. I trained yolov3-tiny.con15 and darknet.conv54 weights that were previously trained on ImageNet dataset. When both weights were trained, the model that was retrained in yolov3-tiny.conv 15 had less averagee loss so I chose this model to use in the project. Then, I installed ros+opencv in raspberry pi. Raspberry pi was used because the counter UAV radar system project's main focus was creating drone detecting system that is affordable in price. I wrote a code that reads message from "operate" topic, and if "init" message is subscribed the raspberry pi initiates camera and the net. When "start" message is subscribed it begins detecting the object in a camera frame and sends frames to "img_camera" topic. The classifier_camera node subscribes "img_camera" topic and republishes to "realtime_camera" topic if the "operate" message received has start value. Also, if it reads start value it stores, detected frame locally for later use to process summary image. If "operate" meessage has end value, it processes summary. It analyzies gathered frames, detectes direction of drone from first "start" message subscribed until "end" message was subscribed. Then it sends the information through "summary_camera" topic.<br/><br/>

The code was tested well and worked well. Later I would simply have to improve the performance of model. 

  
<br><br><br>

#### Kyeongnam Kim
In this project, drone will be automatically controlled from side to side about 5 meters using a program called **Ground Station**, not humans.  
So, My role is to control drones automatically using Ground Station.  
I'm going to use DJI Phantom 2(Drone) and UgCS(Ground Station Software).
* [DJI Phantom2](https://www.dji.com/phantom-2)<br>
I'm learning about drone preparation and drone control with Kar Ee. According to Kar Ee, the drone will have a green light if it's calibration in the area where the GPS is caught. Since I have been banned from flying drones from K-Square's conference room, I plan to fly drone from Professor Tony's farm. I'm going to ask Professor Tony that whether I can fly drones on his farm after learning some basic drone control.
* [UgCS](https://www.ugcs.com/)
```
UgCS is one of the Ground Station Software, and this provides easier control than other ground stations.  
It can communicate and control multiple drones at the same time, 
and it has built-in no-fly zones around all major airports. 
Users can also create a no-fly zone.
```
I'm currently researching how to connect laptops-smartphones-DJI Phantom2 while learning how to use UgCS. I'm going to try again because the connection between the laptop and the drone was successful, but the connection between the smartphone and the drone was unsuccessful. Also, I am going to investigate whether I can adjust ground station without my smartphone.  
The connection method will be organized on [Wiki](https://github.com/seonghapark/cuav/wiki).


<br/><br>
#### Inbae Kang
- My role in this project is the ROS part. ROS is a system that defines the nodes that play each role and defines the topics and messages so that they can communicate with each other smoothly. So far, I have designed the overall design on the ROS of the Counter UAV Project, defined the necessary messages, topics, and nodes, and are implementing each node and message in code.<br/><br>

- In implementing a Decision node that announces the start of a cycle and receives the results, there was a synchronization problem when receiving messages from both nodes, which was solved by threading. I implemented Decision and Storage nodes, but the result message format is not yet confirmed in Camera and Radar, so I used String from std_msgs package. In the case of the Storage node, when the message is received, a file with the current time is created and stored in a subdirectory in the main package. In addition, the basic ROS code of the camera node is implemented to make the camera part work faster.<br/><br>
  
- So far, I have had trouble installing ROS Kinetic on the Raspberry Pi, but it is currently resolved. In addition, I plan to write shell scripts to build an environment for testing and to specify test scenarios and rehearsals. I also plan to write custom messages and materialize the code as the message types for each part become specific.

#### Youngjin  

We're trying to detect UAV using radar and camera. In this system, radar and camera are used to identify object in surveillance area.

This is Radar team. We receive data from radar, which is moving over the connected rail. Rail starts moving one end of the side and moves to the other end of the side. Velocity of moving rail should be constant. When rail finishes move side to side, one SAR image data is produced. We use this image to classify the object in front of radar. Our goal is classify 4 kinds of object, Human, Car, UAV, and etc.

I took part of analyzing python codes.  Under this paragraph is explaining how ROS nodes work, how data are move, how SAR image is generate.

---

# Get Data From Radar (0_get_data.py)

- When 'radar start' signal received, send 'start moving' signal to rail. After signal is sended to rail, radar begins to receive data. Received data are Stacked until rail finishes move one side to the other side. When rail sends signal of 'finish movement', publish stacked data to 'BYTE Array' form.

# Analyze and Parse Raw data (2_analyzer.py)

- Analyzer waits until raw data is passed by data receiver(0_get_data.py). When data arrive, parse raw data into two part, sync and data. Under this paragraph is form and characteristics of binary data

    ---

    First Byte           | Second Byte

    0b'00SDDDDD' | 0b'110DDDDD'

    ---

    S : Sync, 0 or 1 to distinguish True portion of Data

    D : Data  

    ---

- Receiver module of radar receive produces 10-bit data and divide those data to two bytes. Each byte has half of data. Combine these Two bytes and produce one pair of output, 'sync and data'. After finish parsing, Publish parsed data.

# Process data and make SAR image (make_sar_image.py)

- This node waits until parsed data is passed by analyzer(2_analyzer.py). It makes SAR image from parsed data. There are Three steps to make SAR images.
    1. Get SAR frame
        - Use sync to separate Frame. There should be long enough period of silence between sync, so we have to set threshold of silence length. After setting minimum silence length, find regions where length between two syncs are over minimum silence length. These regions are where we slice data to get SAR frame. Each region, slice data for get SAR frame. Important thing is use the **second complete positive-valued period** in the region. After slicing data, take Hilbert Transform of each frame. When finishes get SAR frames, subtract mean of all SAR frames from each frames. It gets rid of DC phase component which occurred from transmit-to-receive antenna.
    2. Range Migration Algorithm(RMA)
        - Apply RMA to SAR frames, Produces SAR image.
    3. Plot image
        - Plotting image to user. We use this image to classify objects(UAV, Car, Human, etc.), So publish image data to classifier.

# Classify object using SAR image

- Probability of using CNN or RNN to classify objects from image data. It can be decided when we succeed at making SAR image.

---

## Things to do

- I succeed transferring data between nodes in ROS. But some reason, SAR image doesn't come out, I think this is because difference of radar between MIT's and ours. I need to adjust parameters such as sample rate, radio frequency, pulse period. After adjusting these parameters, I wish SAR image comes out properly.

p.s. I tried to study Range Migration Algorithm, but it's bit too hard for me.. haha..

### I looked for some reference for that, and I think this would help to understand the concept: https://pdfs.semanticscholar.org/2db7/070ca6eb79c289fb515067c25c9ce3de1cab.pdf. What I understand is RMA is a set of methods to modify raw radar data with regard its angular and linear movement to illustrate the results in one image (plot).

---


**Haeeun** <br/>

I took part of test radar. 
Before the test, I try to understand and construct the ROS node of radar. Then I changed `get_data.py` to ROS. I performed field test to check the radar and we could check some facts through it. The results are under the documents. 
Now I'm changing `draw.py` to ROS for checking figure of raw data from radar.


### Indoor
It was tested in the conference room. A person moved back and forth with an iron plate(about 30x30).
![image](https://user-images.githubusercontent.com/44107947/66231980-d182f380-e6b5-11e9-808c-be64434d26ab.png)
![image](https://user-images.githubusercontent.com/44107947/66231988-d8116b00-e6b5-11e9-8572-15e8a708d1ba.png)


### Outdoor
I tested at empty place between K-SW Square and Anvil. It is assumed that it can recognize things in about 12m. A person moved back and forth with an iron plate(about 30x30).
Next, I changed the heigt of antenna. The result 3 was measured holding by hand and the height is about 120cm. I could see that noise was reduced than when the radar was on the table. It is not sure that the reason is the table or height of the radar, but I requested that a rail will be over 120cm.

**1. Nothing**
![image](https://user-images.githubusercontent.com/44107947/66232011-e5c6f080-e6b5-11e9-9f76-61325392820f.png)

**2. Moving back and forth**
![image](https://user-images.githubusercontent.com/44107947/66232031-ef505880-e6b5-11e9-9d61-a481e8b915c3.png)
![image](https://user-images.githubusercontent.com/44107947/66232035-f5463980-e6b5-11e9-9632-be1b4356e5e3.png)

**3. Changing antenna height (around 120cm)**
![image](https://user-images.githubusercontent.com/44107947/66232048-fd05de00-e6b5-11e9-8a80-5f24dd806123.png)

**4. Moving back and forth in 120cm**
![image](https://user-images.githubusercontent.com/44107947/66232059-03945580-e6b6-11e9-9b95-439c666f6e94.png)


After fall break, I'll complete changing code and test on the rail. I think that I need to check the specific time of delay  for making SAR image. Additionally I'll test to find height and condition for reducing noise of radar.

<br/>

**Kyungyeon Park**

I was in charge of making rail. There are not a lot of components in KSQ, so I have to buy all the components. But the components are late and the progress is being delayed. First, I ordered the motor and the motor driver and assembled it with the Raspberry Pi. Next, I ordered the power adapter and the ball screw and connected it with the motor, the motor driver and the Raspberry Pi. I tried to use the robot profile in KSQ as a rail support, but it didn't match with the ball screw so I ordered a new 30mm x 60mm profile. I expect new items to arrive by the end of the fall break. The supporter on which the radar will be placed will be printed out by the 3D printer, fixed in the profile with bearings and screwed in the nut housing (ball screw nut) (see figure below).

<img src="https://i.ibb.co/g4NmHqD/rail.jpg" width="50%">

The parts came slowly, so in advance, I calculated some data about the step that stepper motor needs to go one round and the step that stepper needs to go 1 inch. I've been experimenting with the python code to see whether the motor is running exactly one round, and it seems to run one round. But I think I need to think about how to prove this exactly. The calculation is correct, but there seems to be a little error due to friction.

Next, I installed ROS on the raspberry pi of the rail to be used to control the stepper motor. Previously I used Raspbian Buster as my OS for Raspberry Pi, but when I installed ROS Kinetic on Raspbian buster, I kept getting an error. So I used Raspbian Jessie for my OS and I could successfully install ROS on the Raspberry Pi. Also, I installed the ROS on the Raspberry Pi of the camera side.

The process of connecting wires and making rails is detailed in the [Making rail Wiki](https://github.com/seonghapark/cuav/wiki/Making-Rail). I would appreciate it for your reference.

After the fall break, I will assemble the profile, ball screw and nut housing I ordered today. Also, I will talk with the Radar team about how to allocate the radar and make the radar suppoter with a 3d printer.


---

# **Inbae Kang**

## 1.Structure
![structure](https://i.imgur.com/poalF5m.jpg)

## 2.Rehearsal
  1. ROSCORE is run on the main package. The rest of the rail / radar nodes and camera nodes run a shell script to set up the execution environment. Main Raspberry Pi is localhost and Camera and Radar Raspberry Pi are configured to communicate on ROS by setting ROS_MASTER_URI to the IP address of main Raspberry Pi / PC.
  2. Each node is executed in camera and radar Raspberry Pi (by shell script named <package_name> .sh), log, storage, web nodes are executed in order in main package, finally decision node is executed. Send an init message to the operate topic.
  3. The rail and camera packages complete their initialization, and the rail node sends a message to the rail_end topic indicating that the rail has finished initializing. The decision node receiving the message goes from the init phase to the start phase.
  4. The Decision node sends a start message to the operate topic.
  5. The three nodes that received the message 1. The rail node moves the rail over 74 seconds. 2. The radar node starts collecting binary data. 2. The Camera node starts collecting data. While collecting data, the Decision node receives real-time data through the realtime_camera topic, stores it in the storage node, and passes the file path and result value to the web node to show the result_web topic.
  6. When the rail reaches the end, it posts a message to the rail_end topic that the cycle is over and the decision node that receives the message goes to the end phase.
  7. The decision node subscribed to that topic sends a message to the end topic telling the camera and radar to stop collecting data.
  8. The radar package publishes the binary data accumulated so far to the raw topic. The storage node stores the raw file.
  9. Publish for make_sar_image node to receive after conversion to IFFT and wav data.
  10. Create a SAR image and pass it to the decision node
  11. The Camera package creates a summary of the photos so far and sends a message to the summary_camera.
  12. RADAR and CAMERA publish to the result_radar and summary_camera topics, respectively, so that the Decision node receives it and delivers it to the storage node.
 
## 3.Message Definition

### Radar Package

- radar/railstart : 데이터 수집을 시작하기 위해서 Rail이 움직이도록 보내는 메시지
```
    bool start
    bool direction #움직일 방향
```
- radar/railstop : 레일이 끝에 도달하여 끝났다는 것을 알리기 위한 메시지.
```
    bool terminate
```
- radar/raw : 수집된 raw데이터.
```
    uint8[] data
    uint64 num #데이터 잘랐을 때, 디버깅용으로 사용.
```
- radar/wav : 변환된 데이터
```
    uint16[] data #두번째 5bit가 여기
    uint16[] sync #첫번째 3bit가 여기
    uint64 num #위와 동일
    uint64 sr #sample rate
```
- radar/result_radar → sensor_msgs/Image

### Camera Pacakage

- camera/sendframe
```
    float64[] coords
    float64 percent
    string operate
    sensor_msgs/Image frame
```
- camera/sendsummary
```
    float64 percent
    string direction
    sensor_msgs/Image frame
```
### Rail Package

- rail_end → std_msgs/String

### Main Pacakge

- main/operate,end
```
    string command
    bool direction
```
- main/result
```
    float64 percent_camera
    float64[] coords_camera
    float64 percent_radar
    sensor_msgs/Image image_camera
    sensor_msgs/Image image_radar
    string direction
```
- main/realtime
```
    float64[] coords
    float64 percent
    sensor_msgs/Image frame
```
- main/result_web
```
    float64 percent_camera
    float64[] coords_camera
    float64 percent_radar
    string image_camera
    string image_radar
    string direction
```
- log → std_msgs/String
