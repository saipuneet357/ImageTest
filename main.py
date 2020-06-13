import face_filter
import text_recog

image_name = "pig_nose.png"
face_data_points = "shape_predictor_68_face_landmarks.dat"


def main():

    text = text_recog.text_recognition_from_video()
    print(text)
    face_filter.pig_filter(image_name, face_data_points)


if __name__ == "__main__":
    main()
