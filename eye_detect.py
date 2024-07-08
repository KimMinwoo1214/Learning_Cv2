# import cv2

# # 카메라 준비
# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# # cap.set(3, 640)  # width
# # cap.set(4, 480)  # height

# # 카메라 읽기
# while True:
#     # 프레임을 이미지로 읽어들임
#     _, frame = cap.read()
    
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
#         # 얼굴 영역을 잘라서 그 부분에서 눈을 찾기
#         roi_gray = gray_frame[y: y+h, x:x+w]
#         roi_color = frame[y: y+h, x:x+w]

#         eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5, minSize=(10, 10), maxSize=(50, 50))

#         if len(eyes) >= 2:
#             eye_list = sorted(eyes, key=lambda eye: eye[0])
#             left_eye = eye_list[0]
#             right_eye = eye_list[1]

#             eye_x1 = left_eye[0]
#             eye_y1 = left_eye[1]
#             eye_x2 = right_eye[0] + right_eye[2]
#             eye_y2 = right_eye[1] + right_eye[3]

#             cv2.rectangle(roi_color, (eye_x1, eye_y1), (eye_x2, eye_y2), (0, 0, 0), -1)

#     # 결과 보여주기
#     cv2.imshow('Video', frame)

#     # 키보드 q가 눌렸을 때,
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np

def pair_eyes(eyes):
    paired_eyes = []
    eyes = sorted(eyes, key=lambda x: x[0])  # x 좌표 기준으로 정렬
    i = 0
    while i < len(eyes) - 1:
        # 현재 눈과 다음 눈이 충분히 가까운지 확인하여 쌍으로 묶기
        x1, y1, w1, h1 = eyes[i]
        x2, y2, w2, h2 = eyes[i + 1]
        if abs(x2 - (x1 + w1)) < w1:
            paired_eyes.append(((x1, y1, w1, h1), (x2, y2, w2, h2)))
            i += 2  
        else:
            i += 1  
    return paired_eyes

def overlay_image_alpha(img, img_overlay, x, y, alpha_mask):
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to do
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    img_crop = img[y1:y2, x1:x2]
    img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
    alpha = alpha_mask[y1o:y2o, x1o:x2o, None]

    img_crop[:] = alpha * img_overlay_crop + (1 - alpha) * img_crop

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

sunglass_img = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y: y+h, x:x+w]
        roi_color = frame[y: y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5, minSize=(10, 10))

        paired_eyes = pair_eyes(eyes)

        for (eye1, eye2) in paired_eyes:
            ex1, ey1, ew1, eh1 = eye1
            ex2, ey2, ew2, eh2 = eye2

            top_left_x = min(ex1, ex2)
            top_left_y = min(ey1, ey2)
            bottom_right_x = max(ex1 + ew1, ex2 + ew2)
            bottom_right_y = max(ey1 + eh1, ey2 + eh2)

            # 선글라스 이미지 크기 조정
            sunglass_resized = cv2.resize(sunglass_img, (bottom_right_x - top_left_x, bottom_right_y - top_left_y))

            alpha_s = sunglass_resized[:, :, 3] / 255.0
            sunglass_resized = sunglass_resized[:, :, :3]

            overlay_image_alpha(roi_color, sunglass_resized, top_left_x, top_left_y, alpha_s)

    cv2.imshow("Video", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()