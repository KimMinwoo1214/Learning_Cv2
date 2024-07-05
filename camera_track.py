import cv2

cap = cv2.VideoCapture(0)

def callBack(value):
    pass

# img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (5,5), 1)

cv2.namedWindow("Control Green")
# cv2.createTrackbar("high_t", "Control Blur", 10, 255, callBack)
cv2.createTrackbar('G', 'Control Green', 0, 255, callBack)

while True:
    _, frame = cap.read()

    g = cv2.getTrackbarPos('G', 'Control Green')
    
    frame[:, :, 1] = g

    # high_t = cv2.getTrackbarPos("high_t", "Control Blur")
    # img_canny = cv2.Canny(cam_blur, 10, high_t )

    cv2.imshow("frame", frame)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()