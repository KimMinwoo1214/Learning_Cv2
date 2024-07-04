import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 100)
low = 50
high = 150


while True:
    _, frame = cap.read()
  
    # frame = cv2.flip(frame, -1)
    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    # change_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny_frame = cv2.Canny(gray_frame, low, high)
    blur_frame = cv2.GaussianBlur(frame, (11, 11), 10)
    
    cv2.imshow("Video", frame)
    cv2.imshow("Gray frame", gray_frame)
    cv2.imshow("Canny frame", canny_frame)
    cv2.imshow("Blur frame", blur_frame)
    # cv2.imshow("YUV Frame", yuv_frame)
    # cv2.imshow("Change Frame", change_frame)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()