
# 김도진

My role for this project was to create an object detection model that can detect drone, car, and person. At the beginning, I wrote a python code that reads a video or webcam and detects objects that are defined in COCO dataset.

--> Did you test with a video? Where did you get the video from? Who recorded video? What objects were there? What do you mean that "objects that are defined in COCO dataset"? The objects in the COCO classese? Then What are in the COCO classes? What objects did you detect from the video exactly?

### Reply
I used the video downloaded from youtube [DJI PHANTOM 4 RTK – A Game Changer for Construction Surveying](https://www.youtube.com/watch?v=tAuF5aZi1ic). The video was too long, I only maintained video frames that contain drones and removed others. 

COCO dataset has 80 object categories such as person, car, bus and etc. Categories that are in COCO dataset can be found in this site: [COCO labels](https://github.com/pjreddie/darknet/blob/master/data/coco.names). The purpose of running the code was simply to check whether the code loads yolo weight well and detects objects that are in 80 category.


I wrote 3 codes, which are codes that detect objects with pre-trained yolov and yolov3-tiny models using opencv DNN, Pytorch, and Tensorflow.
  
--> What are the combination of the 3 codes? tiny YOLO and tensorflow, tiny YOLO and Pytorch? What are the results of that in terms of training loss, training accuracy, valivation loss, and validation accuracy? What are the accuracy of evaluation result? How deep is the net? What are the parameters of tiny YOLO and YOLOv3? Why do you pick the two ML model in detail (any reference)?

### Reply
I used both Yolov3 and Yolov3-tiny models, loaded these models in opencv DNN, Pytorch, and Tensorflow to do object detection. I referred to [Object Detection Comparison](https://medium.com/@jonathan_hui/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359) when choosing which model to use. The performance of each models are well described in this article. I used pre-defined network, yolov3 has 75 convolutional layers and yolov3-tiny has 15 layers. 
  
Compared performance of each codes and concluded that if not using the GPU while inferring, using opencv DNN is the fastest.

--> Provide graph data of the result. Background must be white, add title in each axis, font size of title be big. Leave the plotting code and input data as a txt file in a folder (make a new folder in this git).

### Reply
I did not get about how to plot the graph data.

I ended up using yolov3 and yolov3-tiny because it is much faster than faster rcnn or mask rcnn.

--> Why that is faster then rcnns? Explain it in details. And also where the processing is time consuming (inference step or drawing step, etc)

### Reply
I chose yolov3 because it is one of the fastest object detection model. Even though overall accuracy is worse than faster-rcnn, when detecting large objects it performs similarly. Faster RCNN looks the complete image and predicts objects with region proposals. On the other hand, Yolo does not look at the complete image. It divides the image into n*n grids (the bigger n is accuracy increases but slows down). In grids it takes bounding boxes and the network outputs class probability for the bounding box. This step differentiates two models. Since yolo does not look for the object in the complete image it is faster. 

After figuring out what framework to use, I searched for image datasets to train yolov3.

--> Framework here is maybe the ML model and tool configuration?

### Reply
Thus, I concluded to use opencv DNN and yolov3 for camera detection.

I found about 2600 drone images from github and about 2600 person & car images from Pascal VOC dataset.

--> Where did you fint the drone images? Please leave the github address here.

### Reply
[Drone images](https://github.com/chuanenlin/drone-net)

I converted Pascal VOC dataset labels into YOLO format.

--> Why and how did you do that? Can't you just use the images rightaway? Where is the code? Explain the process in detail.

### Reply
COCO datasets were extremely large (about 20GB), so I searched for smaller datasets that are already labelled. This is because labelling thousands of images by myself would take a very long time. Pascal VOC dataset was not very large and it was already labelled, so I decided to use it. One problem was that this dataset had different label format from YOLO. Therefore, I used [convert2Yolo](https://github.com/ssaru/convert2Yolo) github repository to convert Pascal VOC dataset labels into YOLO format. 

While converting to YOLO format, imprecise labels were generated so I looked all images and fixed labels.

--> Why the imprecise labels were generated? Who generated them? How that was happened? How did you fixed the labels?


### Reply
Pascal VOC labels contained 20 categories, but I needed only person and car. Thus, I after converting to YOLO format I looked for images that did not contain either person or car and removed those. Another problem was that the position of the object in the image was described in floating number but only 3 digits were displayed after decimal point(ex. 0 0.712 0.464 0.352 0.271). When I opened the image using the github repository [labelImg](https://github.com/tzutalin/labelImg), I found out that position of boxes were quite imprecise due to the problem I mentioned. I looked over all images to correct the position. 


After dataset was prepared, I used google colab to train custom classes. 
I used google colab because training process required GPU but I did not have one.

--> Why you have to use GPU? Why not only with CPUs? What was the learning rate and how much time required with CPUs for training?

--> Do you think that is reason of CPU and GPU? Not memory? Why did you come up with that you need GPU?
Google colab provided free GPUs for 12hours per session. Training dataset took about 18 hours.<br/>

--> How much of CPUs, GPUs, and memory? How did you come up with trained model when it took 18 hrs and Google provides 12 hrs?


### Reply
After dataset was prepared, I used google colab to train custom classes. I used google colab because training process takes a long time and the time can be diminished using GPU. Image processing requires a lot of computation and GPU is faster than CPU when doing computation (referred to article [GPU vs CPU](https://medium.com/@shachishah.ce/do-we-really-need-gpu-for-deep-learning-47042c02efe2)). This is the reason for choosing google colab instead trying to do training in my computer's CPU. I set the learnig rate to 0.001 and trained for 6000 batches, 64 images each for a batch. It took about 3 hours to train 1000 batches, since I set to 6000 batches the total training time took 18 hours. Google colab provides free GPU for 12 hours per session. Thus, I saved weight every 1000 batches, so when the session expired I again began from previously saved weight.


In coming weeks, I will install ros in raspberry pi and upload custom-trained yolo weights, detection codes to the device.

--> Why are you using raspberry pi? What's the reason that you need the device?

### Reply
I chose to use raspberry pi and camera module to detect objects because the counter UAV radar system projects was mainly focusing on detecting drones precisely in affordable price. Raspberry pi is a affordable device that has fine computational power. 

I will test how well the model detects objects.

--> How will you test? What is the test procedure for it? 

### Reply
I do not have specific standard about how to measure the performance. For now I will try detecting drones in videos with drones that I will download from youtube. Later, if it seems to detect quite well I will find how performance of object detection model is measured and apply to my model.

If the accuracy is low I will figure out other ways to enhance the performance.

--> What accuracy range is "low"? How do you determine that? How would you enhance the performance?

### Reply
Usually accuracy of object detecion model is meassured with [mAP(mean Average)](https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173). If the rate is low I will try to train the model with more images or try to change the parameter of the net. Currently, I am not sure which parameter I should modify.

Also, I will integrate camera detection system with ros nodes. If everything is set I will help radar team for analyzing the SAR image using machine learning. I am not familiar with ros so integrating might be difficult, but I will ask other teammates who are familiar with ros to solve the problem.

--> What is the design of the data flow and data analysis flor of the camera node and camera node related nodes?

### Reply
Overall process of camera detection would be as follows:

1. Receive start signal from main node.
2. Read image frame from the camera.
3. Send the frame through yolov3 network.
4. Receive detection output from the network.
5. Send position information of drone, image frame with bouding box drawn on it to the main node

--> GREAT!

Below is gif showing how drones are detected using pre-trained yolo drone weight

[Drone-detection](https://i.imgur.com/5UL6AvU.gifv)

--> Rander that as a gif or mp4 or wav or other type and upload the result in this git

Below is repository I am working on for camera detection

[drone_detection Repo](https://github.com/dojinkimm/drone_detection)

--> Sync this repository to a foler (make a folder here for you) with the same name in this repository weekly

# Kyeongnam

My role in this project is to control drones automatically.
I'm going to use DJI Phantom 2(Drone) and UgCS(Ground Station Software).
#### Original Text
* UgCS: I'm currently researching how to connect laptops-smartphones-DJI Phantom2 while learning how to use UgCS. I'm going to try again because the connection between the laptop and the drone was successful, but the connection between the smartphone and the drone was unsuccessful. Also, I am going to investigate whether I can adjust ground station without my smartphone.
- [ ] --> What does UgCS provide for the project? Why did you come up with the system? What is the advantages of using the system?
- [ ] --> Why a smartphone is required? can you also explain how those are connected? Is using a smartphone worth?
* DJI Phantom2: I'm learning about drone preparation and drone control with Kar Ee. According to Kar Ee, the drone will have a green light if it's calibration in the area where the GPS is caught. Since I have been banned from flying drones from K-Square's conference room, I plan to fly drone from Professor Tony's farm. I'm going to ask Professor Tony that whether I can fly drones on his farm after learning some basic drone control.
- [ ] --> I think the best step is 1) practice flying drone with Kal Ee, 2) practice the same in the drone park with Kal Ee, and 3) if needed, ask Tony to use his farm. My suggestion is while you are working on those three steps, try using the simulation to do the same. Make sure the software works fine with the simulation. Then, it should not be a big problem to fly drone using the program.
#### [Modify 10/10/2019](https://github.com/seonghapark/cuav/blob/fall2019/README.md)
