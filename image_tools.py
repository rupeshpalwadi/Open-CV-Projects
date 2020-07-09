import cv2
import numpy as np

img = cv2.imread("myimage.png")
print(img.shape)

imgResize = cv2.resize(img,(300,300))
print(imgResize.shape)

imgCropped = img[0:900, 0:600]

cv2.imshow("image", img)
cv2.imshow("image Resize", imgResize)
cv2.imshow("image Cropped", imgCropped)

cv2.waitKey(0)