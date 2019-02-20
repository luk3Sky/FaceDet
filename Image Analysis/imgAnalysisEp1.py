import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('david.jpg', cv2.IMREAD_GRAYSCALE)

# opencv uses BGRA colors

# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

cv2.imshow('david image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt uses RBG colors
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

# Save an image
# cv2.imwrite('david2.jpg', img)