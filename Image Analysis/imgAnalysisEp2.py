import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('david.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('david image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
