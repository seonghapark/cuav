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
