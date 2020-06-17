
import numpy as np
import cv2


# def book_recognition_from_video():
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    # Grayscale, Gaussian blur

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_frame, (3, 3), 0)

    # First find border of objects and then morph close to close internal noise
    edged = cv2.Canny(blur, 10, 250)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total = 0
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if the approximated contour has four points, then assume that the
        # contour is a book -- a book is a rectangle and thus has four vertices
        if len(approx) == 4:
            cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
            total += 1

    if total > 1:
        cr = frame
        cv2.destroyAllWindows()
        break

while(True):
    print(total)
    cv2.imshow('cr', cr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# return total
