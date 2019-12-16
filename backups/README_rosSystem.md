ROS_system
=======
## How to start counterUAV

### Download and set permission
```
$ sudo mkdir -p /home/project
$ sudo chmod 777 /home/project
$ cd /home/project/
```

전체 프로젝트를 다운받으려면

```
$ git clone https://github.com/seonghapark/cuav.git
$ git checkout fall2019
```

이 브랜치만 다운받으려면
```
$ git clone -b fall2019 --single-branch https://github.com/seonghapark/cuav.git
```


### NTP(Network Time Protocol) 설정
```
$ sudo apt-get install -y chrony ntpdate
$ sudo ntpdate -q ntp.ubuntu.com
```


### ROS Kinetic 설치
**한번에 설치 가능**
```
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh
```

[출처] ROS Kinetic 1줄 설치! (오픈소스 소프트웨어 & 하드웨어: 로봇 기술 공유 카페 (오로카)) |작성자 표윤석



### ros 실행

```
$ roscore
```

새로운 터미널을 연 뒤
`/home/project/counterUAV/ROS_system/catkin_ws` 에서
```
$ rosrun ros_counteruav scripts/start.sh
```




---------

## counter UAV ROS system 입니다

### 반드시 우분투 기준 


### 
byte array를 쓰고 싶어요<br>
1. #!/usr/bin/env python3<br>
2. testdata.msg 생성 후 uint8[] some_int // 파이썬3에서는 uint8이 byte고 uint8[]이 bytes이다.
3. from ros_counteruav.msg import testdata  // <br> [ros msg형태](http://wiki.ros.org/msg), [ros array 사용하기](https://answers.ros.org/question/9471/how-to-recieve-an-array-over-publisher-and-subscriber-python/)<br>
4. radar_send = rospy.Publisher('radar_send', testdata, queue_size=1) // 퍼블리셔<br>
5. message.some_int = read_line // 메시지에 데이터 저장 testdata.msg 안에 uint8[] <변수명> 요거 적어주면 된다.<br>
6. rospy.Subscriber('radar_send', testdata, callback) // subscriber <br>
링크를 클릭해 보심 더 빠릅니다.
