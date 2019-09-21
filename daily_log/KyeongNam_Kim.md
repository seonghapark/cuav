# Daily log of Kyeongnam Kim

## 2019-09-04 ~ 2019-09-08
|날짜|내용|
|:--:|:--:|
|2019-09-04 **Wed**| **구체적인 주제 회의**<br> -센서 개발<br> - 센서 개발<br> - 웹 인터페이스<br> - 데이터 전송 딜레이 최적화<br> - ROS 및 웹 연동|
|2019-09-05 **Thr**| **논문 읽기**<br>Accessible Synthetic Aperture Radar System for Autonomous Vehicle Sensing|
|2019-09-06 **Fri**|windows10에서 파일을 실행하려고 시도했으나,<br>오류가 나서 노트북에 Ubuntu 18.04 LTS버전을 새로 설치함|

<br><br><br>

## 2019-09-09 ~ 2019-09-15
|날짜|내용|
|:--:|:--:|
|2019-09-09 **Mon**|Ubuntu에서 파일 실행 성공: 실행 시 bashrc설정 > rosrun|
|2019-09-10 **Tue**|**논문 읽기**<br>Combination of Radar and Audio Sensors for Identification<br>of Rotor-type Unmanned Aerial Vehicles (UAVs)<br><br>ROS_system 코드 분석|
|2019-09-11 **Wed**|**[역할: 드론 제어]**<br> - DJI Phantom2 확보<br> - 베터리 확보 <br> - groundstation 확보 <br> - control manual tutorial 숙지<br><br>드론에 대한 전반적인 기본지식 공부|
|2019-09-12 **Thr**|**조사**<br> - DJI Phantom2 & 베터리: 모델은 확인하였으나, 오작동이 있음<br> - 드론 실험 장소: Anthony 교수님네 농장에서 할 수 있는지 직접 확인 맡기<br> - control manual tutorial: [[link](https://www.dronezon.com/diy-drone-repair-videos/dji-innovation-drones/dji-ground-station-app-setting-up-phantom-2-waypoint-tutorial/)] 읽어보기<br><br>Eric 교수님께 여쭤본 결과, Parrot모델을 사용하는 것이 더 적합하다는 답장을 받음|
|2019-09-13 **Fri**|**조사**<br> - DJI Phantom2에 대해 좀 더 알아보기: groundstation, SDK <br> - Parrot 알아보기: SDK구축 후 IOS 시뮬레이터를 사용하여 개발하는 것까지 알아냄<br><br>Eric 교수님과 대화 나눠보기: Phantom2 -> groundstation로 쉽게 조작 가능(5~10m), re-programming이 아닌 기존의 sw를 이용해 제어입력<br>다른 모델 사용은 어떤가 또한 여쭤보기|

<br><br><br>

## 2019-09-16 ~ 2019-09-22
|날짜|내용|
|:--:|:--:|
|2019-09-16 **Mon**|**조사**<br> DJI Phantom2와 Parrot드론 자동 제어에 대해 조사 [[조사내용](https://www.notion.so/kkyy0126/Drone-d0a25a86697b49c4b291fe0baea0b49e)]|
|2019-09-17 **Tue**|**조사**<br> Ground Station을 중심으로 조사 [[조사내용](https://www.notion.so/kkyy0126/Drone-d0a25a86697b49c4b291fe0baea0b49e)] <br><br> - **SDK**: 개발을 **처음**부터 만드는 것을 기준으로 작성됨.<br>즉, **Ground Station을 사용**하는 것이 시간, 효율적으로 좋다는 결론을 내림<br><br> - **Ground Station**: Mission Planner와 UgCS 중 하나를 사용하는 것이 좋을 듯<br> * Mission Planner: 가장 먼저 만들어진 GCS이며 가장 완전한 기능을 갖춤 <br> * UgCS: 쉬운 GCS, 비행 금지 구역이 내장됨+만들 수 있음|
|2019-09-18 **Wed**|**조사**<br>Mission Planner와 UgCS를 설치하여 비교한 결과, **UgCS**를 사용하는 것이 낫다는 결론을 내림<br>이후 UgCS 사용법에 대해 조사|
|2019-09-19 **Thr**|**사용법 조사**<br>**UgCS**의 사용법에 대해 조사 후, 직접 경로를 만들어 실행시켜봄(시뮬레이션)<br>![successsssss](https://user-images.githubusercontent.com/38516906/65274900-68ff1880-daf2-11e9-91a3-83570acd133b.gif)|
|2019-09-20 **Fri**|**사용법 조사**<br>**UgCS**의 사용법 정리중|

<br><br><br>

## 2019-09-23 ~ 2019-09-29
|날짜|내용|
|:--:|:--:|
|2019-09-23 **Mon**||
|2019-09-24 **Tue**||
|2019-09-25 **Wed**||
|2019-09-26 **Thr**||
|2019-09-27 **Fri**||
