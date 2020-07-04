import text_recog
import text_search
import numpy as np
import cv2


# photo book
image = cv2.imread("bookpairblackb.jpg")
image = cv2.resize(image, (600, 900))
size = image.shape[0:2]
# s = image.shape
# print(s)
# print(size)
black_image = np.zeros(size, np.uint8)
# Grayscale, Gaussian blur

gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray_frame, (1, 1), 0)

# First find border of objects and then morph close to close internal noise
edged = cv2.Canny(gray_frame, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
(cnts, _) = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

total = 0
# for c in cnts:
#     # approximate the contour
#
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#
#     # if the approximated contour has four points, then assume that the
#     # contour is a book -- a book is a rectangle and thus has four vertices
#     if len(approx) == 4:
#         cv2.drawContours(image, [approx], -1, (0, 0, 255), 4)
#         total += 1
peri = cv2.arcLength(cnts[3], True)
approx = cv2.approxPolyDP(cnts[3], 0.02 * peri, True)
cv2.drawContours(black_image, [approx], -1, (255, 255, 255), -1, cv2.LINE_AA)
res = cv2.bitwise_and(image, image, mask=black_image)
rect = cv2.boundingRect(approx)
cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
white_image = np.ones_like(image, np.uint8)*255
reverse_mask = cv2.bitwise_not(white_image, white_image, mask=black_image)
result = reverse_mask+res

invert, text = text_recog.text_recognition_from_text(result)

text_search.crawl(text)

# sites = text_search.list_of_sites(text)
#
# for site in sites:
#     print(site)

while(True):
    cv2.imshow('blackimage', result)
    cv2.imshow('invert', invert)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# for i in range(len(cnts)):
#     cv2.drawContours(image, cnts, i, (0, 255, 0), 3)
#     cv2.imshow('image', image)
#     if cv2.waitKey(3000) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#     print(len(cnts[i]))
# 126
# 1156
# 348
# 1839
# 4232
# 1


# for i in range(len(cnts[3])):
#     cv2.drawContours(image, cnts[3], i, (0, 255, 0), 3)
#     cv2.imshow('image', image)
#     if cv2.waitKey(1000) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#     if 0xFF == ord('u'):
#         break
#
# print(cnts[3])
# print(total)
# while(True):
#     cv2.imshow('image', image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# invert,text = text_recog.text_recognition_from_text()
#
# print(total)
# print(text)
#
# while(True):
#     cv2.imshow('image', image)
#     cv2.imshow('edged', edged)
#     cv2.imshow('closed', closed)
#     cv2.imshow('closed', gray_frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
