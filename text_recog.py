import pytesseract
import cv2.cv2 as cv2
import numpy as np


pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\PUNEETH\\AppData\\Local\\Tesseract-OCR\\tesseract'


def text_recognition_from_video():
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        _, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Grayscale, Gaussian blur, Otsu's threshold

        gray_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray_frame, (7, 9), 0)
        ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Morph open to remove noise and invert image
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        invert = 255 - opening
        data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
        cv2.imshow('frame', frame)
        cv2.imshow('gray_frame', gray_frame)
        cv2.imshow('blur', blur)
        cv2.imshow('thresh', thresh)
        cv2.imshow('opening', opening)
        cv2.imshow('invert', invert)
        if data == 'CHANAKYA\nNEETI':
            return data

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return


def text_recognition_from_text(image):

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Grayscale, Gaussian blur, Otsu's threshold

    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image, (7, 9), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')

    return invert, data
