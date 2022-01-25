import cv2

img = cv2.imread("flower.jpeg")
img=cv2.resize(img, (150,150))

img=cv2.imwrite("112.png",img)