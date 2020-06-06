import face_filter

image_name = "pig_nose.png"
face_data_points = "shape_predictor_68_face_landmarks.dat"


def main():
    face_filter.pig_filter(image_name, face_data_points)


if __name__ == "__main__":
    main()
