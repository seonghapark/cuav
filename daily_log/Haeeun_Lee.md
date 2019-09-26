# Daily log of Haeeun Lee

### 2019.09.05
1. 논문을 읽고 팀원들과 내용 공유
	- CNN_radar

### 2019.09.06
1. raw_data 디렉토리의 1_read_data.py 실행
	- rabbitMQ 대시보드까지 확인했으나 바이너리 파일 변환 결과는 확인 못함.
2. ros 설치 시도	
	- mac OS에 설치 시도
	- ubuntn vm에 설치 시도

### 2019.09.09
1. vmware Fusion에 ubuntu 18.04, ROS melodic 설치 후 실행
2. ROS 공부

### 2019.09.10
1. radar_audio 논문 읽기
2. 코드 분석

### 2019.09.11
1. vmware Fusion에 ubuntu 16.04, ROS kinetice으로 다시 설치
2. 코드 분석

### 2019.09.12
1. make_sar_image.py 실행
2. make_sar_image.py 코드 분석
3. SAR, FMCW 등 개념 조사

### 2019.09.13
1. 회의를 통해 앞으로 해야 할 일들에 대한 정리
2. make_sar_image.py 코드 분석 및 사용된 라이브러리 공부 
3. 안테나 확인

### 2019.09.16
1. 레이더 연결 후 코드 실행 확인
2. matplotlib 라이브러리 관련하여 코드를 실행하면 컴퓨터가 꺼지는 오류가 발생해서 찾아보았지만 아직 해결하지 못함

### 2019.09.17
1. 어제 발생했던 오류 해결
2. ROS 튜토리얼로 기본 통신 구조 확인
3. 참고할 코드 및 수정해야 할 코드 확인하고 이전 프로젝트 모델 분석 및 디렉토리 수정
4. 모델 구조 작성

### 2019.09.18
1. radar 패키지 및 raw 메시지 생성
2. ros 패키지 생성 및 커스텀 메시지 생성하는 법 md로 정리
3. msg import 되지 않는 문제 해결 필요

### 2019.09.19
1. raw 데이터 생성해서 ros로 publish 하는 코드 작성 (0_r_get_data.py 수정)

### 2019.09.20
1. 0_get_data.py 코드 수정 후 실행되는 것 확인

### 2019.09.23
1. ros 관련 코드 python3 사용하도록 변경
2. 수정된 코드에 따라 ros 패키지 구조 변경 중 
3. make_sar_image.py python3로 수정 중

### 2019.09.24
1. make_sar_impage.py python3로 수정
2. 변경된 패키지 구조 및 메시지에 맞게 0_get_data.py 수정
3. git conflict 해결해야 함

### 2019.09.25
1. 레이더 필드 테스트

### 2019.09.26
1. analyzer.py, make_sar_image.py 코드 분석
2. binary 데이터 분석
