import cv2
import numpy as np

img = cv2.imread("mountain.jpg")

# 1) Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9 , 9)

# 2) Color
color = cv2.bilateralFilter(img, 9, 100, 100)

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Cartoon", cartoon)
cv2.waitKey(33)
input('')



