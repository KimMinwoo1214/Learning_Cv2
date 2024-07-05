# import cv2
# import numpy as np

# # 이미지를 읽어옵니다.
# image = cv2.imread('goggle.jpg')

# roi = image[100:600, 300:770, :]

# # 이미지를 그레이스케일로 변환합니다.
# gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# # 이진화 처리 (Thresholding)
# ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# # 컨투어를 찾습니다.
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # 원본 이미지에 컨투어를 그립니다.
# cv2.drawContours(roi, contours, -1, (0, 255, 0), 2)

# # 결과를 화면에 표시합니다.
# cv2.imshow('Contours', roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

src = cv2.imread("goggle.jpg", cv2.IMREAD_COLOR)
roi = src[100:600, 300:770, :]

gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(roi, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(roi, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("src", roi)
    cv2.waitKey(0)

cv2.destroyAllWindows()
