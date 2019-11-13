import cv2
from main.msg import result

class DecisionClass:
    def __init__(self):
        self.coordinates = [0.0, 0.0]
        self.percent_camera = 0.0
        self.percent_radar = 0.0
        self.image_camera = None
        self.image_radar = None
        self.direction = ""

    def generate_message(self):
        msg = result()
        msg.coords_camera = self.coordinates
        msg.percent_camera = self.percent_camera
        msg.percent_radar = self.percent_radar
        msg.image_camera = self.image_camera
        msg.image_radar = self.image_radar
        msg.direction = self.direction

        return msg
