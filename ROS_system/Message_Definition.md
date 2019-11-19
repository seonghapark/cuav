# Message Definition

### Radar Package

- radar/railstart : 데이터 수집을 시작하기 위해서 Rail이 움직이도록 보내는 메시지

    bool start
    bool direction #움직일 방향

- radar/railstop : 레일이 끝에 도달하여 끝났다는 것을 알리기 위한 메시지.

    bool terminate

- radar/raw : 수집된 raw데이터.

    uint8[] data
    uint64 num #데이터 잘랐을 때, 디버깅용으로 사용.

- radar/wav : 변환된 데이터

    uint16[] data #두번째 5bit가 여기
    uint16[] sync #첫번째 3bit가 여기
    uint64 num #위와 동일
    uint64 sr #sample rate

- radar/img
- radar/result

### Main Pacakge

- main/start : 데이터 수집 및 처리, 결과 보고까지 한 주기의 시작을 위한 메시지.
    - 사실 내용은 상관이 없어보인다. std_msgs의 String 이용해도 될 것 같다.
- main/result : 결과를 보여주기 위한 메시지
    -
