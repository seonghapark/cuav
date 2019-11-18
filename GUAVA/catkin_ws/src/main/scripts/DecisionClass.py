from main.msg import result, result_web


class DecisionClass:
    def __init__(self, coordinates=(0.0, 0.0), percent_camera=0.0, percent_radar=0.0,
                 image_camera=None, image_radar=None, direction="",
                 image_radar_name="", image_camera_name=""):
        self.coordinates = coordinates
        self.percent_camera = percent_camera
        self.percent_radar = percent_radar
        self.image_camera = image_camera
        self.image_radar = image_radar
        self.direction = direction
        self.image_radar_name = image_radar_name
        self.image_camera_name = image_camera_name

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



