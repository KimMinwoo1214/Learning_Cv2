import cv2
import numpy as np

path = 'cat1.jpg'
low = 50
high = 100

image = cv2.imread(path)
# print(image.shape)
# print(image.shape[0])

# center_y = image.shape[0] // 2
# center_x = image.shape[1] // 2

# cv2.circle(image, (center_x, center_y), 50, (0, 0, 255), -1)

canny_image = cv2.Canny(image, low, high)
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
image[:, :, 0] = 0
image[:, :, 1] = 0

cv2.imshow("Cat", image)
cv2.imshow("Canny Image", canny_image)
cv2.imshow("YUV Cat", yuv_image)

cv2.waitKey()
cv2.destroyAllWindows()