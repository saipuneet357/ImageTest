import cv2.cv2 as cv2
import boundary as b
import test as t

# image_name = "pig_nose.png"
# face_data_points = "shape_predictor_68_face_landmarks.dat"
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
_, r = cap.read()
frame_boundary = b.center_boundary(r, r.shape)
cap.release()


def switch(key):
    switcher = {
        ord('q'): print(frame_boundary),
        ord('a'): 'exit'
    }
    return switcher.get(key, "nothing")


def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while(True):
        _, frame = cap.read()
        cv2.rectangle(frame, frame_boundary[0], frame_boundary[1], (0, 255, 0), 1)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if switch(key) == 'exit':
            break
        # if cv2.waitKey(1) == ord('q'):
        #     print(frame_boundary)
        #     # text, image = t.object_scan(frame[frame_boundary[0][0]:frame_boundary[1]
        #     #                                   [0], frame_boundary[0][1]:frame_boundary[1][1]])
        #     # print(text)
        #     # cv2.imshow('img', image)

    cap.release()
    cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    main()
