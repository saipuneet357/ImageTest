import text_recog
import text_search
import numpy as np
import cv2


def object_scan(object):
    # photo book
    object = cv2.resize(object, (600, 900))
    size = object.shape[0:2]
    black_image = np.zeros(size, np.uint8)
    # Grayscale, Gaussian blur
    gray_frame = cv2.cvtColor(object, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_frame, (1, 1), 0)

    # First find border of objects and then morph close to close internal noise
    edged = cv2.Canny(gray_frame, 10, 250)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    (cnts, _) = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    peri = cv2.arcLength(cnts[3], True)
    approx = cv2.approxPolyDP(cnts[3], 0.02 * peri, True)
    cv2.drawContours(black_image, [approx], -1, (255, 255, 255), -1, cv2.LINE_AA)
    res = cv2.bitwise_and(object, object, mask=black_image)
    rect = cv2.boundingRect(approx)
    cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
    white_image = np.ones_like(object, np.uint8)*255
    reverse_mask = cv2.bitwise_not(white_image, white_image, mask=black_image)
    result = reverse_mask+res

    _, text = text_recog.text_recognition_from_text(result)
    text_search.crawl(text)
    text_image = cv2.imread("chanakya.jpg")
    return text, text_image
