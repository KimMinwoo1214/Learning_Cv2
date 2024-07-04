import cv2
import numpy as np

def callBack1(value):
    pass

def callBack2(value):
    pass

path1 = 'Beach.jpg'

img1 = cv2.imread(path1)

cv2.namedWindow("Stylish")
cv2.createTrackbar("Sigma_S", "Stylish", 0, 200, callBack1)
cv2.createTrackbar("Sigma_R", "Stylish", 0, 100, callBack2)  # Sigma_R 범위를 0-100으로 설정

while True:
    Sigma_S = cv2.getTrackbarPos("Sigma_S", "Stylish")
    Sigma_R = cv2.getTrackbarPos("Sigma_R", "Stylish") / 100.0  # Sigma_R을 0-1 범위로 변환
    
    img_stylish = cv2.stylization(img1, sigma_s = Sigma_S, sigma_r = Sigma_R)

    cv2.imshow("Stylish", img_stylish)
    
    if cv2.waitKey(1) & 0xff == ord('q'):  # cv2.waitKey(1)을 사용하여 루프를 유지
        break

cv2.destroyAllWindows()
