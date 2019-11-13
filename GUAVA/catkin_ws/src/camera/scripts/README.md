# drone_detection
Drone detection using yolo-tiny

### camera.sh

shell script file responsible for running python files in ros by time.


### get_frame.py

1. receives `init` message from start
    - initialize network, camera
2. when `start` message is received, object detection operates. Frame with bounding box + confidence of detected object + coordinates of objects are published to `img_camera` topic.
3. when `end` message is received, same process happens as step2, but `end` message is included to published message


### classifier_camera.py

1. when message is received from `img_camera` topic, and it has `start` command, it directly published the image to `realtime_camera` topic.
2. when message received has `end` command, it begins summary process. After results are returned it publishes to `summary_camera` topic
    
     
### detection_boxes.py

1. receives network output of yolo-tiny.
2. saves data(class_id, coords, confidence) that have higher confidence level than given threshold.
3. draws bounding boxes


### camera_log.py

- responsible for creating log information, publish it, and print it on the console.

### process_img.py

1. in one black background, images of detected object is merged to the background. (e.g. 3 detected images, then 3 layers are added to the background)
2. if position of an object is different in first frame and last frame, calculate the direction. 
3. confidence is calculated for gathered frames
4. return newly created frame, percent, direction