import cv2
import numpy as np

def callBack(val):
    pass

path1 = "coke.jpg"

img1 = cv2.imread(path1)

# roi = img1[100:600, 300:770, :]

hsv_roi = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

cv2.namedWindow("Change HSV")
cv2.createTrackbar('low_H', 'Change HSV', 0, 179, callBack)
cv2.createTrackbar('high_H', 'Change HSV', 179, 179, callBack)
cv2.createTrackbar('low_S', 'Change HSV', 0, 250, callBack)
cv2.createTrackbar('high_S', 'Change HSV', 255, 255, callBack)
cv2.createTrackbar('low_V', 'Change HSV', 0, 255, callBack)
cv2.createTrackbar('high_V', 'Change HSV', 255, 255, callBack)

while True:    
    low_H = cv2.getTrackbarPos('low_H', 'Change HSV')
    high_H = cv2.getTrackbarPos('high_H', 'Change HSV')
    low_S = cv2.getTrackbarPos('low_S', 'Change HSV')
    high_S = cv2.getTrackbarPos('high_S', 'Change HSV')
    low_V = cv2.getTrackbarPos('low_V', 'Change HSV')
    high_V = cv2.getTrackbarPos('high_V', 'Change HSV')
    
    low = np.array([low_H, low_S, low_V])
    high = np.array([high_H, high_S, high_V])
    
    mask = cv2.inRange(hsv_roi, low, high)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 1000:
            cv2.drawContours(img1, [max_contour], -1, (0, 255,0), 2)
    
    bitwise_and = cv2.bitwise_and(img1, img1, mask=mask)

    cv2.imshow("Coke", img1)
    cv2.imshow("Masking", bitwise_and)
    
    if cv2.waitKey(10) & 0xff == 27:
        break
    
    if cv2.waitKey(10) & 0xff == ord('s'):
        hsv = [low, high]
        np.save("HSV_Value", hsv)
        print("Save successful")

cv2.destroyAllWindows()
