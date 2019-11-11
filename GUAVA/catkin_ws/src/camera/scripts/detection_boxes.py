#!/usr/bin/env python3
import cv2
import numpy as np

STANDARD_COLORS = [
    (255, 248, 240), (230, 224, 176), (0, 255, 127)
]


def get_class_names(label_path):
    with open(label_path, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')
    return classes if classes else None


class DetectBoxes:
    def __init__(self, label_path, confidence_threshold=0.5, nms_threshold=0):
        self.classes = get_class_names(label_path)
        self.confThreshold = confidence_threshold
        self.nmsThreshold = nms_threshold

    # detect bounding boxes from given frame
    def detect_bounding_boxes(self, frame, output):
        '''
        frame: frame from video or webcam
        output: detected information generated from darknet
        '''
        height = frame.shape[0]
        width = frame.shape[1]

        if self.nmsThreshold is not 0:
            return self.detect_yolo(frame, output, width, height)
        return None, None, None

    def detect_yolo(self, frame, output, frame_width, frame_height):
        '''
        frame: frame from video or webcam
        output: detected information generated from darknet
        frame_width: width of frame
        frame_height: height of frame
        '''
        # Search for all bounding boxes
        # Save bounding box that have higher score than given confidence threshold
        class_ids = []
        confidences = []
        boxes = []
        for out in output:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > self.confThreshold:
                    center_x = int(detection[0] * frame_width)
                    center_y = int(detection[1] * frame_height)
                    width = int(detection[2] * frame_width)
                    height = int(detection[3] * frame_height)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([left, top, width, height])

        # Using non-maximum suppression remove overlapping boxes
        # with low confidence
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confThreshold, self.nmsThreshold)
        labels, percentage, coords = [], [], []
        for i in indices:
            i = i[0]
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            # add labels
            labels.append(self.classes[class_ids[i]])
            # add percentage
            percentage.append(confidences[i])
            # add coords
            coords.append([left, top, left+width, top+height])
            self.draw_boxes(frame, class_ids[i], confidences[i], left, top, left + width, top + height)

        if len(confidences) > 0:
            max_conf_idx = confidences.index(max(confidences))
            return labels[max_conf_idx], percentage[max_conf_idx], coords[max_conf_idx]
        return "", 0.0, []

    # draw boxes higher than confidence threshold
    def draw_boxes(self, frame, class_id, conf, left, top, right, bottom):
        '''
        frame: frame from video or webcam
        class_id: class index that detected object belongs
        conf: confidence of the detected object
        left: left coord
        top: top coord
        right: right coord
        bottom: bottom coord
        '''
        color, txt_color = ((0, 0, 0), (0, 0, 0))
        label = '{}%'.format(round((conf*100), 1))
        if self.classes:
            assert (class_id < len(self.classes))
            label = '%s %s' % (self.classes[class_id], label)
            color = STANDARD_COLORS[class_id % len(STANDARD_COLORS)]

        if sum(color) < 500:
            txt_color = (255, 255, 255)

        # draw a bounding box
        cv2.rectangle(frame, (left, top), (right, bottom), color=color, thickness=3)

        # put label on top of detected bounding box
        label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        top = max(top, label_size[1])
        cv2.rectangle(frame, (left, top - round(1.5 * label_size[1])),
                      (left + round(1.5 * label_size[0]), top + base_line),
                      color=color, thickness=cv2.FILLED)
        cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color=txt_color, thickness=2)
