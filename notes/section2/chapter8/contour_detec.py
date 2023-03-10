import numpy as np
import cv2


# contor is the curve joining a  sequence of points defining the boundary of an object
# in an image, therefore, contours are key information for object boundaries
# used in object detection, shape analysis and object recognition


# in order to find contours, we must first apply a threshold technique
# to make the image binary

# image, contours, hierarchy = cv2.findContours(image, mode, method, contours, hierarchy, offset)

# Load the image
img = cv2.imread('./images/couple.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Display the image
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# common countour modes are:

# cv2.RETR_EXTERNAL - returns only external contours
# cv2.RETR_LIST - returns external and internal contours
# many others

# compressing contours - contours can be compressed in order
# to diminish the number of points
# the compressing algorythms are set in the "method" parameter
# cv2.CHAIN_APPROX_NONE means that no compression is performed
# cv2.CHAIN_APPROX_SIMPLE can be used to compress, it compresses
# vertical, horizontal and diagonal segments of the contour
# more complex methods like teh-chim are also available, those are better
# because they can compute the geometrical importance of a point

# Load image in grayscale
img = cv2.imread('./images/couple.jpg', cv2.IMREAD_GRAYSCALE)

# threashold
ret1, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_OTSU)

# Apply the Teh-Chin algorithm to find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Show the original image with contours
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()