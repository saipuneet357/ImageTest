import cv2.cv2 as cv2
import numpy as np
import dlib
from math import hypot


def main():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    nose_image = cv2.imread("pig_nose.png")
    while(True):
        # Capture frame-by-frame
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(frame)

        for face in faces:
            landmarks = predictor(gray_frame, face)

            top_nose = (landmarks.part(29).x, landmarks.part(29).y)
            center_nose = (landmarks.part(30).x, landmarks.part(30).y)
            left_nose = (landmarks.part(31).x, landmarks.part(31).y)
            right_nose = (landmarks.part(35).x, landmarks.part(35).y)
            nose_width = int(hypot(left_nose[0]-right_nose[0], left_nose[1]-right_nose[1])*1.2)
            nose_height = int(nose_width*0.77)
            nose_pig = cv2.resize(nose_image, (nose_width, nose_height))
            top_left = (int(center_nose[0]-nose_width/2), int(center_nose[1]-nose_height/2))
            bottom_right = (int(center_nose[0]+nose_width/2), int(center_nose[1]+nose_height/2))
            nose_area = frame[top_left[1]:top_left[1] +
                              nose_height, top_left[0]:top_left[0]+nose_width]
            nose_pig_gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
            _, nose_mask = cv2.threshold(nose_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)
            nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
            nose_final = cv2.bitwise_or(nose_area_no_nose, nose_pig)

            frame[top_left[1]:top_left[1] +
                  nose_height, top_left[0]:top_left[0]+nose_width] = nose_final

            cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
