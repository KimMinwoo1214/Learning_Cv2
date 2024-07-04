import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
  
    # frame = cv2.flip(frame, -1)
    change_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # canny_frame = cv2.Canny(gray_frame, low, high)
    # blur_frame = cv2.GaussianBlur(frame, (11, 11), 10)
    
    cv2.imshow("Video", frame)
    # cv2.imshow("Gray frame", gray_frame)
    # cv2.imshow("Canny frame", canny_frame)
    # cv2.imshow("Blur frame", blur_frame)
    # cv2.imshow("YUV Frame", yuv_frame)
    cv2.imshow("Change Frame", change_frame)
    
    if cv2.waitKey(10) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()