import numpy as np
import cv2.cv2 as cv2


def center_boundary(frame, shape):
    h = shape[0]
    w = shape[1]
    top_left = (int(3*w/8), int(h/4))
    bottom_right = (int(5*w/8), int(3*h/4))
    return [top_left, bottom_right]
