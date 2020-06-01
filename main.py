import cv2.cv2 as cv2
import numpy as np



def main():
    img = cv2.imread(r'C:\Users\PUNEETH\Downloads\IMG_20190629_151046.jpg')
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(img)
     

if __name__ == "__main__":
    main()