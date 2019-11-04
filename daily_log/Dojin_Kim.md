# Daily log of Dojin Kim

## 2019-09-04 ~ 2019-09-13

### 2019-09-04
* 구체적인 주제 회의
  - 센서 개발
  - 웹 인터페이스
  - 데이터 전송 딜레이 최적화
  - ROS 및 웹 연동
  
### 2019-09-05
* 논문 읽기
  - "An Approach for Reducing Computational Time for Real-Time Autonomous Vehicle Tracking"

### 2019-09-06
* 기존 코드 run해보기
  - ROS_system에 있는 코드 run하기 위해 환경설정하기
  - VMWare로 Ubuntu 설치
  
### 2019-09-09
  - VMWare Ubuntu에 설치 완료
  - ROS_system에 있는 코드 run 완료
  - docker로 ROS 설치 
  
### 2019-09-10
  - docker로 ROS 설치 및 코드 클론 성공, 그러나 코드 run 실패
  - Combination of Radar and Audio Sensors for Identification of Rotor-type Unmanned Aerial Vehicles (UAVs) 논문 읽기

### 2019-09-11
  - Project내 역할 분배
  - DJI phantom dataset image 획득
  
### 2019-09-12
  - DJI phantom dataset image 획득 및 정리. 
  - Training set 500, Test set 200 확보함
  
### 2019-09-13
  - parrot dataset image 획득 및 정리
  - 기존 coco dataset에 pre-trained된 yolov3모델에 새로운 class 추가하는 방법 찾기
  - tensorflow yolov3로 object detection 하는 프로그램 test
  
## 2019-09-16 ~ 2019-09-20

### 2019-09-16
  - yolov3-tiny에 custom class 추가 시도
  - 100개 data labelling 완료
  
### 2019-09-17
  - [drone-net](https://github.com/chuanenlin/drone-net) 에서 약 2600장에 학습된 yolo 모델 발견
  - 해당 모델로 opencv dnn과 pytorch에서 drone detection 성공 (tensorflow는 오류 발생)
    => 정확도 높여야함<br/>
    
    [Drone-detection](https://i.imgur.com/5UL6AvU.gifv)


  - [drone_detection Repo](https://github.com/dojinkimm/drone_detection)에 작업중인 코드 업로드
  - 라즈베리파이와 카메라 확보, 모니터와 HDMI선 구매해야함 
  

### 2019-09-18
  - 라즈베리파이 OS 설치 및 카메라 장착
  - 기존 [drone_detection Repo](https://github.com/dojinkimm/drone_detection) clone 받아서 코드 실행
    - torch 설치 Fail
    - opencv DNN으로 영상 detection 프로그램 run 됐으나 1초에 1프레임도 안나옴
  - 웹캠 실행해봤으나 매우 느림, 개선할 수 있는 방법 찾아봐야 함
  
### 2019-09-19
  - 라즈베리파이에서 opencv dnn으로 drone detect 프로그램 실행 (약 0.5FPS)
  - Pytorch와 Tensoflow로 해보려고 시도
  - 파이썬 버전이 꼬여서 수정중
  - 기존 컴퓨터에서는 opencv dnn이 pytorch, tensorflow보다 빠름
  
### 2019-09-20
  - FPS 높일 방법 찾아봄
  - ROS에서 opencv 실행할 때 고려해야할 점들 찾아봄
  
  
## 2019-09-23 ~ 2019-09-27

### 2019-09-23
  - 라즈베리파이에 ROS 설치, 
  - ROS와 opencv 사용하는 법 찾아봄
  - 학습시킬 데이터 수집
  
### 2019-09-24
  - 라즈베리파이 ROS 설치 실패
  - Colab으로 학습 시도 중

### 2019-09-25
  - Colab으로 yolo tiny 드론 학습 완료 확인
  - Feature extraction을 사용하기 위해 coco dataset 다운로드 및 정리
  - Colab으로 yolov3 학습하기 위해 필요한 dataset, cfg, data, names 파일들 정리

### 2019-09-26
  - drone, person, car labelling 작업
  - pascal voc 사진들 변경
  
### 2019-09-27
  - drone, person, car labelling 라벨링 완료
    - 약 드론 2600장, 사람+차량 2500장
  - colab에서 yolov3에 학습
  
## 2019-09-30 ~ 2019-10-04

### 2019-09-30
  - colab으로 yolov3 6시간 걸쳐서 학습, 정확도가 다소 낮음
  - Pascal VOC 데이터셋이 YOLO로 변환되는 과정에서 라벨링에 오류가 조금 있음을 발견
  - 모든 이미지 라벨링 체크하려는 중 - 900장 라벨링 수정 완료, 4000장 정도 더 남음...

### 2019-10-01
  - 라벨링 완료
  - colab으로 yolov3 학습시작....아마 저녁 11시쯤 학습 끝날 예정
  

### 2019-10-02
  - colab으로 yolov3 학습에 에러가 나서 다시 학습 시작, 이전에 비해 한 batch당 시간이 늘어서 12시간 정도 걸릴것으로 예상
  - radar팀 CNN 도움을 줄 수 도 있기에 CNN 공부
  
## 2019-10-10 ~ 2019-10-11

### 2019-10-10
  - Feedback 받고 README 수정
  - Handson ML 
  
## 2019-10-15 ~ 2019-10-18

### 2019-10-15
  - ROS 설치된 라즈베리파이에 opencv 설치 시도.... troubleshooting 중
 
### 2019-10-16
	- Camera node 코드 작성
	- Railstart하면 yolo network load하고 frame들과 detect된 object이름들을 저장한 다음에 railstop때 publish하는 코드 작성

### 2019-10-17
	- camera ros코드 작성 완료
	- 테스트 위해 ROS설치된 라즈베리파이에 opencv 설치하려고 했으나,,,,,실패

### 2019-10-18
	- 라즈베리파이 초기화하고 다시 설치 및 opencv 재설치 시도

## 2019-10-21 ~ 2019-10-25

### 2019-10-21
	- 라즈베리파이에 opencv 3.4 설치 완료
	- ROS camera node design 일부 수정
		- get_frame node는 동일
		- classifier_camera가 2개의 topic에 다른 정보 publish
			- 하나는 realtime으로 image와 object detect된 정보를 publish
			- 다른 하나는 SAR image가 한 cycle을 돌고 신호를 주면 지금까지 detect된 frame들과 object들을 분석 및 요약해서 publish

### 2019-10-22
	- get_frame 코드 작성
		- Object detect하고 detect되서 bounding box그린 frame, detect된 object의 label, 확률 publish
	- classifier_camera 코드 작성
		- 실시간으로 받은 frame바로 publish
		- rail end 가 True라는 것을 subscribe하면 지금까지 받은 frame들 분석(이 부분 아직 하지 못함)및 publish


### 2019-10-23
	- ROS 코드 실행 위해 환경 configure (CMakeList, package.xml 수정)
	- gnome-terminal 설치, roscore, rosrun 실행환경 구축
	- cv_bridge 설치 시도했으나 실패(이 부분만 성공하면 camera코드 실행될 것 같음)

### 2019-10-24
  - cv_bridge, sensor_msgs 직접 github에서 다운 받고 패키지 저장, 그러나 catkin_make 실패
	- ROS에 문제가 있을 것 같아서 새롭게 ROS+Raspberry pi 이미지를 다운 받아서 다시 설치 시
	

## 2019-10-28 ~ 2019-11-01

### 2019-10-28
 - 라즈베리파이에 ros-kinetic opencv 설치
 - opencv가 python2 버전으로 설정되어있어서 python3 버전으로 가능하게 수정중

### 2019-10-29
 - python3에서 opencv작동 완료
 - ros node들 작동 완료
 - sh 파일 작성해서 자동으로 모든 script들이 실행되도록 해야함
 - classifier_camera, get_frame 코드 수정

### 2019-10-30
	- fake_start, fake_rail 코드 작성해서 decision node에서 시작을 하는 것과 비슷한 프로세스를 적용함
	- bash 파일을 작성해서 roscore는 백그라운드 나머지는 gterminal로 실행되게 함
	- 현재 수정 필요한 부분:
		- detection후에 bounding box를 그리는 상황에서 type error 발생
		- 만들어진 frame ros msg 포맷으로 convert시 error 발생
		- 기존 drone만 detect하는 tiny yolo가 0.2 FPS, 1 frame에 5초 정도가 걸리는 현상 발생, 추후 모델 재학습 혹은 변경 필요함

### 2019-10-31
	- roscore 해서 이미지 detection까지 완성, 그러나 이미지 message로 전송하려고 할 때 에러 발생
	- Pythonpath 오류나서 이미지 재설치
