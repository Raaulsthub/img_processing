import cv2
import numpy as np

# humans are not good in observing changes to gray scale images
# it is possible to color the gray images with pseudo colors

img = cv2.imread('./images/dilma.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()

# recoloring
img_hsv = cv2.applyColorMap(gray_img, cv2.COLORMAP_HSV)
# there are other colormaps available
cv2.imshow('hsv pseudo colored', img_hsv)
cv2.waitKey()
cv2.destroyAllWindows()

# it is also possible to apply custom color maps to an image
