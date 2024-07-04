import cv2
import numpy as np

path2 = 'train_road.jpg'
path1 = 'goggle.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

print(img1.shape)
print(img2.shape)

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
print(img1.shape)

img3 = cv2.add(img1, img2)

mask = np.ones((img2.shape[0], img2.shape[1], 3), dtype = 'uint8') * 50
print(mask.shape)

img3_b = cv2.add(img3, mask)
roi = img1[100:600, 300:770, :]

roi[:, :, 1] = 255

# cv2.imshow("Add DOG", img3)
# cv2.imshow("Maks dog", img3_b)
cv2.imshow("Cut image", roi)

cv2.waitKey()
cv2.destroyAllWindows()