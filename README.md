# GUAVA

## Introduction
This is counter UAV project by fall2019 KSQ students and we will briefly explain our project.

Our goal is detecting stationary drone using radar and camera in daytime and announce through web(flask server). We use both radar and camera to detect UAV because of low cost and high performance. For this, We use rail and radar for making SAR image and using YOLO tiny v3, camera can catch the drone and its movement.

But, the problem is our system can make sar image, but it need to be improved and using RNN or DNN, we have to find out the thing in SAR image is drone or not. Now, we have rail, radar, and camera.

So the remaining roles is improving camera detection, improving making SAR images, detecting drones in SAR image, and announce it through flask server. We wish you good luck.

For more specific information or before starting this project, we ***strongly recommend*** read the documents in [`Documents`](https://github.com/seonghapark/cuav/tree/fall2019/Documents), [`references`](https://github.com/seonghapark/cuav/tree/fall2019/references), and [Wiki](https://github.com/seonghapark/cuav/wiki). 

</br>


## Our Team
* [`Inbae Kang`](https://github.com/cleverdevk) cleverdevk@gmail.com
  * Team leader, ROS
* [`Dojin Kim`](https://github.com/dojinkimm) dojinkim119@gmail.com
  * camera
* [`Haeeun Lee`](https://github.com/ihaeeun) ihaeeun16@gmail.com
  * radar
* [`Kyeongnam Kim`](https://github.com/kimkyeongnam) kkyy0126@naver.com
  * drone, web
* [`Kyungyeon Park`](https://github.com/contestpark) contestpark@naver.com
  * rail, radar
* [`Youngjin Kim`](https://github.com/ANGJIN) zmfjrxmfjr@naver.com
  * radar
  
  
</br>
  
  
## Description of directory
```
cuav - 2019-12-19 ver.
├ Documents
│ └ Rail
├ Flask Server
│ ├ model
│ ├ src
│ ├ static
│ │ ├ assets
│ │ │ ├ fonts
│ │ │ ├ images
│ │ │ │ └ avatars
│ │ │ └ scripts
│ │ └ img
│ └ templates
├ GUAVA
│ ├ catkin_ws 
│ ├ └ src
│ │   ├ camera
│ │   ├ ├ msg
│ │   │ └ scripts
│ │   │   ├ cfg
│ │   │   └ weights
│ │   ├ main
│ │   │ ├ logs
│ │   │ ├ msg
│ │   │ ├ scripts
│ │   │ └ storage
│ │   │   ├ camera_image
│ │   │   ├ final_result
│ │   │   └ raw
│ │   ├ radar
│ │   │ ├ msg
│ │   │ ├ output
│ │   │ ├ scripts
│ │   │ └ test_data 
│ │   ├ rail
│ │   │ ├ scripts
│ │   │ └ temp_rail
│ │   └ vision_opencv
│ └ setup_scripts
├ daily_log
├ references
│ └ radar_sar_rma
├ Progression_2019_09_20.md
├ Progression_2019_10_04.md
└ Progression_2019_11_22.md

```
* **Documents**: Several documents of our system
* **Flask Server**: GUAVA Web server
* **GUAVA**: Our main project is in here
  * catkin_ws : Catkin Workspace of GUAVA  
  * setup_scripts : Python code to start whole system
* **daily_log**: GUAVA team member's daily log
* **references**: Referenced papars
  * radar_sar_rma : Program of making SAR images using a radar of MIT OpenCourseWare


