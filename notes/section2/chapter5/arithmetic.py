import cv2
import numpy as np

# saturation arithmetic
# its a type of arithmetic where the operations are limited to a fixed range
# by restrictiong maximum and minimum values an operation can take
# this is used to clip values in opencv so they never leave the [0, 255] range


# raw img
img = cv2.imread('./images/wilson.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('raw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# adding and subtracting

# adding
add_vector = np.ones(img_gray.shape, dtype='uint8') * 30
brighter = cv2.add(img_gray, add_vector)
cv2.imshow('brighter', brighter)
cv2.waitKey(0)
cv2.destroyAllWindows()
# adding in the colored image
add_vector = np.ones(img.shape, dtype='uint8') * 100
brighter_colored = cv2.add(img, add_vector)
cv2.imshow('brighter and colored', brighter_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()

# subtracting
add_vector = np.ones(img.shape, dtype='uint8') * 130
darker_colored = cv2.subtract(img, add_vector)
cv2.imshow('darker and colored', darker_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()

