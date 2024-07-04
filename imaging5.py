import cv2
import numpy as np

path1 = 'goggle.jpg'

img1 = cv2.imread(path1)

def callBack(value):
    pass

roi = img1[100:600, 300:770, :]

cv2.namedWindow("Cut image")

cv2.createTrackbar('B', 'Cut image', 0, 255, callBack)
cv2.createTrackbar('R', 'Cut image', 0, 255, callBack)
cv2.createTrackbar('G', 'Cut image', 0, 255, callBack)

cv2.setTrackbarPos('B', 'Cut image', 0)
cv2.setTrackbarPos('G', 'Cut image', 0)
cv2.setTrackbarPos('R', 'Cut image', 0)

while True:
    b = cv2.getTrackbarPos('B', 'Cut image')
    g = cv2.getTrackbarPos('G', 'Cut image')
    r = cv2.getTrackbarPos('R', 'Cut image')

    modified_roi = roi.copy()
    modified_roi[:, :, 0] += b
    modified_roi[:, :, 1] += g
    modified_roi[:, :, 2] += r

    cv2.imshow("Cut image", modified_roi)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키를 누르면 루프 종료
        break

cv2.destroyAllWindows()