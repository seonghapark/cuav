# Counter UAV Radar - Fall 2019

Youngjin
Inbae
Kyungyeon 
Haeeun
Kyeongnam

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
  
