import cv2
import numpy as np

def callBack(val):
    pass

# 웹캠 캡처 시작
cap = cv2.VideoCapture(0)

cv2.namedWindow("Change HSV")
cv2.createTrackbar('low_H', 'Change HSV', 0, 179, callBack)
cv2.createTrackbar('high_H', 'Change HSV', 179, 179, callBack)
cv2.createTrackbar('low_S', 'Change HSV', 0, 255, callBack)
cv2.createTrackbar('high_S', 'Change HSV', 255, 255, callBack)
cv2.createTrackbar('low_V', 'Change HSV', 0, 255, callBack)
cv2.createTrackbar('high_V', 'Change HSV', 255, 255, callBack)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # BGR에서 HSV로 변환
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 트랙바에서 값 가져오기
    low_H = cv2.getTrackbarPos('low_H', 'Change HSV')
    high_H = cv2.getTrackbarPos('high_H', 'Change HSV')
    low_S = cv2.getTrackbarPos('low_S', 'Change HSV')
    high_S = cv2.getTrackbarPos('high_S', 'Change HSV')
    low_V = cv2.getTrackbarPos('low_V', 'Change HSV')
    high_V = cv2.getTrackbarPos('high_V', 'Change HSV')

    low = np.array([low_H, low_S, low_V])
    high = np.array([high_H, high_S, high_V])

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
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
    
    if cv2.waitKey(10) & 0xff == ord('s'):
        hsv = [low, high]
        np.save("HSV_detect", hsv)
        print("Save successful")
        
cap.release()
cv2.destroyAllWindows()
