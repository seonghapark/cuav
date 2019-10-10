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
