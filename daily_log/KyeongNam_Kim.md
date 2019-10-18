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
|2019<br>-09-09<br>**Mon**|Ubuntu에서 파일 실행 성공: 실행 시 bashrc설정 > rosrun|
|2019<br>-09-10<br>**Tue**|**논문 읽기**<br>Combination of Radar and Audio Sensors for Identification<br>of Rotor-type Unmanned Aerial Vehicles (UAVs)<br><br>ROS_system 코드 분석|
|2019<br>-09-11<br>**Wed**|**[역할: 드론 제어]**<br> - DJI Phantom2 확보<br> - 베터리 확보 <br> - groundstation 확보 <br> - control manual tutorial 숙지<br><br>드론에 대한 전반적인 기본지식 공부|
|2019<br>-09-12<br>**Thr**|**조사**<br> - DJI Phantom2 & 베터리: 모델은 확인하였으나, 오작동이 있음<br> - 드론 실험 장소: Anthony 교수님네 농장에서 할 수 있는지 직접 확인 맡기<br> - control manual tutorial: [[link](https://www.dronezon.com/diy-drone-repair-videos/dji-innovation-drones/dji-ground-station-app-setting-up-phantom-2-waypoint-tutorial/)] 읽어보기<br><br>Eric 교수님께 여쭤본 결과, Parrot모델을 사용하는 것이 더 적합하다는 답장을 받음|
|2019<br>-09-13<br>**Fri**|**조사**<br> - DJI Phantom2에 대해 좀 더 알아보기: groundstation, SDK <br> - Parrot 알아보기: SDK구축 후 IOS 시뮬레이터를 사용하여 개발하는 것까지 알아냄<br><br>Eric 교수님과 대화 나눠보기: Phantom2 -> groundstation로 쉽게 조작 가능(5~10m), re-programming이 아닌 기존의 sw를 이용해 제어입력<br>다른 모델 사용은 어떤가 또한 여쭤보기|

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
|2019-09-23 **Mon**|**사용법 조사**<br>**UgCS**의 사용법 정리중[[link](https://www.notion.so/kkyy0126/UgCS-529b849fc534436f984a51d8a7b8cca8)]<br><br>컨퍼런스룸의 위경도 좌표 정리<br>![aaa](https://user-images.githubusercontent.com/38516906/65458420-9104b980-de1b-11e9-974c-074829030132.PNG)|
|2019-09-24 **Tue**|**통신기 조사**<br>UgCS에 사용하기 위해서는 2.4GHz 또는 900MHz datalink를 사용해야 함(무선연결)<br>스토리지룸에 2.4GHz Wireless DataLink Module이 존재하여 대여 및 driver 설치<br><br>DJI Phantom2 경로 제작(좌우)<br><br>DJI Phantom2 수령|
|2019-09-25 **Wed**|**DJI Phantom2 공부**<br>DJI Phantom2 베터리, 어뎁터, 충전기, 프로펠러 대여<br>조작방법 공부: 전원 on 및 비행 준비까지의 과정 공부(Kar Ee와 함께 진행)|
|2019-09-26 **Thr**|UgCS 공부: DJI Phantom2와 연동 & 툴 다루기|
|2019-09-27 **Fri**|UgCS 공부<br><br>DJI Phantom2 setup 영상 제작<br>[![video](https://user-images.githubusercontent.com/38516906/65806197-718cca00-e156-11e9-854b-2a711b94e804.jpg)](https://www.youtube.com/watch?v=ZRwFmM1wtMI)|

<br><br><br>

## 2019-09-30 ~ 2019-10-06
|날짜|내용|
|:--:|:--:|
|2019-09-30 **Mon**|**UgCS + DJI Phantom2 연결 시도**<br>스마트폰과 데스크탑 UgCS 연동 성공<br>컨트롤러와의 연동을 위해서는 OTG젠더 필요: 내일 시도 예정|
|2019-10-01 **Tue**|**UgCS + DJI Phantom2 연결 시도**<br>OTG젠더가 보이지 않고 다른 잭을 이용해 시도했으나, 되지 않았음.<br>NAZA라는 것을 사용한 영상이 있어, 현재 조사 중<br><br>드론 연습 자체를 건물 내에서 금지한다는 얘기를 전달받음.<br>토니 교수님네 농장에서 해야할 것 같음|
|2019-10-02 **Wed**|**UgCS + DJI Phantom2 연결 시도**<br>컴퓨터+스마트폰+드론 연동 시도 결과, 컴퓨터에서는 드론이 인식되는데<br>스마트폰에서는 인식이 되지 않음.<br>스마트폰에서 인식이 되도록 하거나, 컴퓨터로만으로도 가능한지 알아봐야 함<br><br>NAZA는 필요없음|
|2019-10-03 **Thr**|UgCS + DJI Phantom2 연결 시도|
|2019-10-04 **Fri**|:fire:Fire Starter:fire:|

<br><br><br>

## 2019-10-07 ~ 2019-10-13
|날짜|내용|
|:--:|:--:|
|2019-10-07 **Mon**|:maple_leaf:Fall Break:maple_leaf:|
|2019-10-08 **Tue**|:maple_leaf:Fall Break:maple_leaf:|
|2019-10-09 **Wed**|:maple_leaf:Fall Break:maple_leaf:|
|2019-10-10 **Thr**|UgCS 관련 Wiki작성 시작(드론+컴퓨터+핸드폰+UgCS)<br>* 준비물 및 기초 단계는 후에 진행 예정|
|2019-10-11 **Fri**|Kar Ee와 드론 조종법 공부<br>드론+컴퓨터+핸드폰+UgCS연동 부분 wiki 작성 중|

<br><br><br>

## 2019-10-14 ~ 2019-10-20
|날짜|내용|
|:--:|:--:|
|2019-10-14 **Mon**|:fire:Fire Starter:fire:|
|2019-10-15 **Tue**|UgCS와 노트북 연동방법 숙지완료, wiki 작성 중|
|2019-10-16 **Wed**|비행 시뮬레이션을 돌리기 위해 연동을 시도하였으나,<br>휴대폰에서 드론 인식이 되지 않아 원인을 알아보는 중|
|2019-10-17 **Thr**|갑자기 인식 자체가 되지 않아 프로그램을 재설치하여 다시 진행 중<br>드론 시뮬운전 연습을 위해 (현재 Phantom2가 인식되지 않아)IRIS로 진행하려고 함|
|2019-10-18 **Fri**||

<br><br><br>

## 2019-10-21 ~ 2019-10-27
|날짜|내용|
|:--:|:--:|
|2019-10-21 **Mon**||
|2019-10-22 **Tue**||
|2019-10-23 **Wed**||
|2019-10-24 **Thr**||
|2019-10-25 **Fri**||
