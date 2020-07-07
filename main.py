import cv2.cv2 as cv2
import boundary as b

image_name = "pig_nose.png"
face_data_points = "shape_predictor_68_face_landmarks.dat"


def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while(True):
        ret, frame = cap.read()
        b.center_boundary(frame, frame.shape)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    main()
