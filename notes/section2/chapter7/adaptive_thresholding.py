import numpy as np
import cv2

# when the image has uneven lighting or illumination conditions,
# the simple thresholding techniques with fixed thresh values
# will often fail, since there will be no fixed value that is gonna
# segment the image perfectly
# the threshold value, than, needs to be adapted locally to account
# for these variations, this is called adaptive thresholding

# the signature for the adaptive th in cv2 is:
# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst

# adaptive methods

# cv2.ADAPTIVE_THRESH_MEAN_C - the thresh value T(x, y) is calculated as the mean of the
# blocksize x blocksize neighborhood of (x, y) minus the C parameter

# cv2.ADAPTIVE_THRESH_GAUSSIAN_C - THE T(x, y) is calculated as the weighted sum of the
# blocksize x blocksize neighborhood of (x, y) minus the C parameter

# thresholdType will be binary or binary_inv

img = cv2.imread('./images/metro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Adaptive Threshold', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

threshold_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Adaptive Threshold', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()