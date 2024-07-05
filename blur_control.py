import cv2
import numpy as np

def callBack(value):
    pass

path1 = 'Lotte.jpg'

img1 = cv2.imread(path1)
img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (5,5), 1)

cv2.namedWindow("Control Blur")
cv2.createTrackbar("high_t", "Control Blur", 10, 255, callBack)

while True:

    high_t = cv2.getTrackbarPos("high_t", "Control Blur")
    img_canny = cv2.Canny(img_blur, 10, high_t )

    cv2.imshow("Lotte", img_canny)

    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
