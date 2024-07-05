import cv2

def callBack(val):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Change Frame")
cv2.createTrackbar('H', 'Change Frame', 0, 179, callBack)
cv2.createTrackbar('S', 'Change Frame', 0, 255, callBack)
cv2.createTrackbar('V', 'Change Frame', 0, 255, callBack)

while True:
    _, frame = cap.read()  
    
    change_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    cv2.imshow("Video", frame)
    cv2.imshow("Change Frame", change_frame)
    
    if cv2.waitKey(10) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()