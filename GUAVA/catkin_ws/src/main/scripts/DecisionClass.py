import cv2
from main.msg import result
from main.msg import result_web
from

class DecisionClass:
    def __init__(self):
        self.coordinates = [0.0, 0.0]
        self.percent_camera = 0.0
        self.percent_radar = 0.0
        self.image_camera = None
        self.image_radar = None
        self.direction = ""
        self.image_radar_name = ""
        self.image_camera_name = ""

    def __init__(self, coordinates, percent_camera, percent_radar, image_camera, image_radar, direction):
        self.coordinates = coordinates
        self.percent_camera = percent_camera
        self.percent_radar = percent_radar
        self.image_camera = image_camera
        self.image_radar = image_radar
        self.direction = direction

    def generate_storage_message(self):
        msg = result()
        msg.coords_camera = self.coordinates
        msg.percent_camera = self.percent_camera
        msg.percent_radar = self.percent_radar
        msg.image_camera = self.image_camera
        msg.image_radar = self.image_radar
        msg.direction = self.direction

        return msg

    def generate_web_message(self):
        msg = result_web()
        msg.coords_camera = self.coordinates
        msg.percent_camera = self.percent_camera
        msg.percent_radar = self.percent_radar
        msg.image_radar = self.image_radar_name
        msg.image_camera = self.image_camera_name

        return msg

