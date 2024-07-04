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

# def on_trackbar_change(val):
#     b = cv2.getTrackbarPos('B', 'Control Blur')
#     g = cv2.getTrackbarPos('G', 'Control Blur')
#     # r = cv2.getTrackbarPos('R', 'Cut image')

#     modified_img1 = img1.copy()
#     modified_img1[:, :, 0] = b
#     modified_img1[:, :, 1] = g
#     # modified_roi[:, :, 2] = r

#     cv2.imshow("Control Blur", modified_img1)

# cv2.createTrackbar('B', 'Control Blur', 0, 255, on_trackbar_change)
# cv2.createTrackbar('G', 'Control Blur', 0, 255, on_trackbar_change)
# # cv2.createTrackbar('R', 'Cut image', 0, 255, on_trackbar_change)

# cv2.setTrackbarPos('B', 'Control Blur', 0)
# cv2.setTrackbarPos('G', 'Control Blur', 0)
# # cv2.setTrackbarPos('R', 'Cut image', 0)

# on_trackbar_change(img1)

while True:

    high_t = cv2.getTrackbarPos("high_t", "Control Blur")
    img_canny = cv2.Canny(img_blur, 10, high_t )

    cv2.imshow("Lotte", img_canny)

    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
