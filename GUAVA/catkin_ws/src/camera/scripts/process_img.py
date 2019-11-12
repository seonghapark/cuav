#!/usr/bin/env python3

import cv2
import numpy as np


class ProcessImage:

    def __init__(self, channels=3):
        self.width = None
        self.height = None
        self.channels = channels

    def process_summary(self, frames, coords, percents):
        self.width, self.height = frames[0].shape[:2]
        frame, direction = self.get_direction(frames, coords)
        percent = self.get_percent(percents)

        return frame, direction, percent

    def get_direction(self, frs, cor):
        """
        frs: frames that contain detected object with bounding boxes
        cor: coordinates of detected object in a frame
        """
        # initialize background with black
        bg = np.zeros([self.width, self.height, self.channels], np.uint8)

        # center coordinate of 1st frame
        before = ((cor[0][2] + cor[0][0]) // 2, (cor[0][3] + cor[0][1]) // 2)
        for idx, f in enumerate(frs):
            left = cor[idx][0]
            top = cor[idx][1]
            right = cor[idx][2]
            bottom = cor[idx][3]

            rect_img = f[top:bottom, left:right]
            bg[top:bottom, left:right] = rect_img

            # cv2.imshow("f", bg)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        # center coordinate of last frame
        # draw line from 1st frame's center coord to last frame's center coord
        after = ((right + left) // 2, (top + bottom) // 2)
        cv2.line(bg, before, after, (0, 0, 255), 5)

        dX = before[0] - after[0]
        dY = before[1] - after[1]
        (dirX, dirY) = ("", "")

        # ensure there is significant movement in the
        # x-direction
        if np.abs(dX) > 20:
            dirX = "East" if np.sign(dX) == 1 else "West"

        # ensure there is significant movement in the
        # y-direction
        if np.abs(dY) > 20:
            dirY = "North" if np.sign(dY) == 1 else "South"

        # handle when both directions are non-empty
        if dirX != "" and dirY != "":
            direction = "{}-{}".format(dirY, dirX)

        # handle when one direction is detected
        elif dirX != "" or dirY != "":
            direction = dirX if dirX != "" else dirY

        # otherwise, object is not moved
        else:
            direction = "Not moved"

        return bg, direction

    def get_percent(self, percent):
        return percent

