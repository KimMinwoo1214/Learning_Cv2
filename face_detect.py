import cv2
import numpy as np

cap = cv2.VideoCapture(0)
f_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    _, frame = cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = f_cascade.detectMultiScale(gray_frame, scaleFactor = 1.3, minNeighbors = 5)

    for (x,y,w,h) in faces:
        rec_frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # roi_gray = gray_frame[y: y+h, x: x+w]
        # roi_color = rec_frame[y: y+h, x: x+w]

    # 결과 보여주기
    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Face Detection", frame)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
