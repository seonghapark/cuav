Youngjin Kim
==================
김영진 팀원의 일지입니다.

2019.09.05
1. 각자 배정된 논문을 읽은 후 세미나를 통해 서로의 논문 내용 공유
- 나에게 배정된 논문 : Object Classification raw radar data using Convolutionl neural networks
2. 내일 해야할 일 : github 에 올라와 있는 sample code들 돌려보고 review 하기

2019.09.06
1. 저번 팀이 했던 코드 및 작업물 실행을 위해 코드 분석 및 실행
2. Ubuntu 에서 실행이 가능하다고 판단하여 Ubuntu설치를 시도하였으나 맥북에 설치가 잘 되지 않음

2019.09.09
1. Mac에서 Ubuntu 사용하기 위해 VMware 설치 후 Ubuntu및 실행환경 Setup
2. 지난 코드 실행 및 결과 확인

2019.09.10
1. radar_audio 논문 읽고 분석 및 토론
2. 내일 있을 화상 미팅에서 이야기할 주제 정리 및 앞으로의 방향 탐색.

2019.09.11
1. 화상 회의를 통해 프로젝트의 구체적인 목표 설정 및 역할 분담
- 내가 맡은 역할 : Radar를 이용하여 SAR을 만들고, 데이터를 받고/가공하여 물체가 무엇인지 판독
2. ROS Kinetic을 사용하기 위해 VMware 에 Ubuntu 16.04 설치 및 ROS 환경 설정.

2019.09.12
1. radar_ros_rma 안에 있는 예시 코드를 실행
2. radar와 sar의 개념에 대한 공부
3. sample code review

2019.09.13
1. 화상 회의를 통해 radar 팀에서 해야할 일들 정리 및 자문 구함.
2. sample code의 colormap 설정 등 code에 사용한 모듈을 공부

2019.09.16
1. Conference Room에서 radar를 작동해 real time으로 데이터를 받아오는것을 실험 및 확인.
2. real time data를 wmv로 변환하여 visualize 하였을 때 어떤식으로 나오는지 확인하였으나 아무것도 나오지 않음.

2019.09.17
1. RabbitMQ로 작성된 코드를 ROS로 변경하여 돌리기 위해 VM 설정 및 ROSKinetic 재설치 후 한줄 설치 코드 README 작성

2019.09.18
1. catkin_ws 생성
2. radar 패키지 생성
3. raw data 교환을 위한 메시지 raw.msg 생성
4. 해야 할 일 : custom message를 생성하였으니 파이썬 코드에서 import를 하여 사용하는 법 찾기

2019.09.19
1. raw data를 받아 parsing 하는 부분 작성
2. parsing후 sar imaging하기 위한 wav로 변환
3. wav data를 ifft 및 sar imaging 하기 위한 전처리 해야 함 

2019.09.20
1. 화상 회의를 통해 radar에서 분업할 부분과 수정해야 할 부분 정립

2019.09.23
1. 개발 환경 Python2 에서 Python3로 변경
2. radar 패키지에 rail 포함 및 통신을 위한 topic 정리
3. radar 없이 실험하기 위한 fake data sender code 작성
4. analyzer code에서 wav파일을 넘겨주기 위해 custom message 작성 및 코드 수정
5. 회의를 통해 전체 프로젝트는 하나의 패키지가 아닌 구분된 패키지로 구성하기로 정함.

2019.09.24
1. make-sar-image.py 코드 분석 및 수정
2. realtime radar 데이터를 가져오기 위한 sample rate 측정 실험 및 data type 설정을 위한 msg 작성
3. 분할해서 작업하던 코드를 병합하여 하나의 패키지로 만드는 과정 진행.

2019.09.25
1. ros을 실행시키기 위한 스크립트인 .launch 생성
2. 야외에서 레이더 위치에 따른 데이터를 수집하기 위한 실험 진행

2019.09.26
1. 화상 회의 진행. 현재까지 진행상황 점검 및 질의응답/멘토링
2. Radar Raw data 의 구조 및 어떤식으로 작동하는 지에 대한 분석
3. sar imaging하기 위해 sync를 어떻게 처리해야 하는지에 대한 구상중.

2019.09.27
1. analyzer 노드와 sar-imaging 노드 사이의 데이터 전송을 위한 custom message 수정 및 데이터 전송이 성공적으로 이루어짐 확인.
2. sar-imaging하기 위한 데이터 전송이 완료되었으므로, sar-imaging 예시 코드를 현재 우리가 가진 레이더 데이터에 맞게 작동하도록 코드 분석 및 수정 필요.
