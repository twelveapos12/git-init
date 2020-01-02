import cv2
import random

img = cv2.imread("processed/36.png")


cv2.imshow("World", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
