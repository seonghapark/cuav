# GUAVA Catkin Workspace

### Environment
- Raspbian Stretch (use in Raspberry PI)
- Ubuntu 16.04 (use in development)
- ROS Kinetic
- Python 3

### Download GUAVA project and set permission
```
$ sudo mkdir -p /home/project
$ sudo chmod 777 /home/project
$ cd /home/project

$ git clone https://github.com/seonghapark/cuav.git
```

### Set NTP(Network Time Protocol)
```
$ sudo apt-get install -y chrony ntpdate
$ sudo ntpdate -q ntp.ubuntu.com
```

## ROS
### Install ROS Kinetic
```
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh
```
[출처] ROS Kinetic 1줄 설치! (오픈소스 소프트웨어 & 하드웨어: 로봇 기술 공유 카페 (오로카)) |작성자 표윤석


### Run ROS
```
$ roscore
```
At `home/project/cuav/GUAVA/catkin_ws` in the new terminal
```
$ rosrun [package_name] [file_name]
```

### Alias
```
alias eb='nano ~/.bashrc'
alias sb='source ~/.bashrc'
alias cw='cd /home/project/cuav/GUAVA/catkin_ws'
alias cs='cd /home/project/cuav/GUAVA/catkin_ws/catkin_ws/src'
alias cm='cd /home/project/cuav/GUAVA/catkin_ws && catkin_make'
source /opt/ros/kinetic/setup.bash
source /home/project/cuav/GUAVA/catkin_ws/devel/setup.bash
export ROS_PACKAGE_PATH=/home/project/cuav/GUAVA/catkin_ws/src/:/opt/ros/kinetic/share
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
```

## Main

## Radar
### How to use radar
1. Connect the usb to the PC.
2. Use 12V battery for power on.
3. After all switches on, check the used port.
  ```
  $ ls /dev/tty [+ tab]
  # Press [tab] instead of [Enter]
  ```
4. Change mod of port
  ```
  $ sudo chmod 777 /dev/[port]
  ```

### How to run radar code
```bash
$ source devel/setup.bash
$ cd /home/project/cuav/GUAVA/catkin_ws/
$ rosrun radar [file_name.py]
```
There is shell script for launching all rada codes. If you want to run with radar, you should use `radar.sh` and you want to run with binary files, you should use `test_radar.sh`.
```bash
$ cd //home/project/cuav/GUAVA/catkin_ws/radar/scripts
$ ./radar.sh
$ ./test_radar.sh
```

## Camera
The command below launches all camera codes needed for progressing the project. It runs `classifier_camera.py` and `get_frame.py` that are responsible for taking frame from camera, detect objects, and publish data.
```bash
$ ./camera.sh
```

The codes run in background, so in order to end execution of process you have to find processes that are running the files and kill it by process id.
```bash
$ ps -ef | grep py
$ kill -9 xxxx xxxx
```
