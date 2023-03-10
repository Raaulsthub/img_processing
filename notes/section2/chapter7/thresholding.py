import numpy as np
import cv2


# image segmentation is communly used to partition an image
# into different regions that ideally correspond to real world
# objects extracted from the background
# threshholding is a simple, yet effective, segmentation method
# the pixels are partitioned depending on their intensity value,
# and so, it can be used to partition an image into a foreground and
# a background. threshholding is a key part of image segmentation.
# the objective of segmentation is turning a complex representation
# of the image into a simple and processing-friendly one

img = cv2.imread('./images/metro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray)
cv2.waitKey()
cv2.destroyAllWindows()

# simple tresholding - based on treshold value, pixels beneath
# it will be black, above will be white
# cv2.treshold (img, tresh_value, maxval, method)
# this function applies a fixed lebel thresholding to the src image

# thresholding types

# cv2.THRESH_BINARY  -> dst(x,y) = max_value if src(x, y) > thresh, 0 otherwise
# dst is the pixel in the output image src is the pixel in the source image
# max value is 255 (if grayscale uint8 is being used)

ret1, thresh1 = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('cv2 treshold bin 50', thresh1)
cv2.waitKey()
cv2.destroyAllWindows()

ret2, thresh2 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('cv2 treshold bin 100', thresh2)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.THRESH_BINARY_INV -> inverse of the binary, if src is > thresh, 0, else, max_value

ret3, thresh3 = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('cv2 thresh bin inv', thresh3)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.THRESH_TRUNC -> dst(x, y) = threshold if src(x, y) > thresh, src(x, y) otherwise

ret4, thresh4 = cv2.threshold(gray, 100, 150, cv2.THRESH_TRUNC)
cv2.imshow('cv2 thresh trunc', thresh4)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.THRESH_TOZERO -> dst(x, y) = src(x, y) if src(x, y) > thresh, 0 otherwise

ret5, thresh5 = cv2.threshold(gray, 150, 255, cv2.THRESH_TOZERO)
cv2.imshow('cv2 thresh tozero', thresh5)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.THRESH_TOZERO_INV -> inverse of tozero

# Special Threshold
# under, there are two thresholds that can be combined
# with the ones above, they can compute the optimal threshold
# value for thresh, they only work with 8bit images

# Apply Otsu thresholding
threshold_value, threshold_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the thresholded image
cv2.imshow('Otsu Threshold', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply triangle thresholding
threshold_value, threshold_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)

# Display the thresholded image
cv2.imshow('triangle Threshold', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# its essencial to reduce noise with gausian or 
# bilateral filters before using thresholding techniques