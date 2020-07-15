import cv2.cv2 as cv2
import boundary as b
import text_recog as t
import requests
import numpy as np

# image_name = "pig_nose.png"
# face_data_points = "shape_predictor_68_face_landmarks.dat"

url = 'http://192.168.43.55:8080/shot.jpg'
r = requests.get(url)
img_arr = np.array(bytearray(r.content), dtype=np.uint8)
r = cv2.imdecode(img_arr, -1)
r = cv2.resize(r, (600, 900))
frame_boundary = b.center_boundary(r, r.shape)


def main():
    while(True):
        r = requests.get(url)
        img_arr = np.array(bytearray(r.content), dtype=np.uint8)
        frame = cv2.imdecode(img_arr, -1)
        frame = cv2.resize(frame, (600, 900))
        cv2.rectangle(frame, frame_boundary[0], frame_boundary[1], (0, 255, 0), 1)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('a'):
            _, text = t.text_recognition_from_text(frame[frame_boundary[0][0]:frame_boundary[1]
                                                         [0], frame_boundary[0][1]:frame_boundary[1][1]])
            print(text)
    cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    main()
