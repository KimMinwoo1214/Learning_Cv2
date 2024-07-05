import cv2
import numpy as np
import os

# 웹캠 캡처 시작
cap = cv2.VideoCapture(0)

# 트랙바 초기값을 설정하기 위해 파일이 있는지 확인
if os.path.exists("HSV_detect.npy"):
    hsv = np.load("HSV_detect.npy", allow_pickle=True)
    low = hsv[0]
    high = hsv[1]
    
else:
    low = np.array([0, 0, 0])
    high = np.array([179, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # BGR에서 HSV로 변환
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 마스크 생성
    mask = cv2.inRange(hsv_frame, low, high)

    # 노이즈 제거를 위한 모폴로지 연산
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # 컨투어 찾기
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 최대 컨투어 그리기
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 1000:
            cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 2)

    # 원본 영상에 마스크 적용
    bitwise_and = cv2.bitwise_and(frame, frame, mask=mask)

    # 결과 보여주기
    cv2.imshow("Masking", bitwise_and)
    cv2.imshow("Original with Contours", frame)
    
    key = cv2.waitKey(10) & 0xff
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
