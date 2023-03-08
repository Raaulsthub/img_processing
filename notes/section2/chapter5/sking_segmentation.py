import cv2
import numpy as np

# Load the image
img = cv2.imread('./images/wilson.png')

# Convert the image to HSV color space, it is used for skin segmentation
# because it separates color info into hue, saturation and value components
# this makes it easier to make a skin color range
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of skin color in HSV
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

# Create a binary mask for the skin area
mask = cv2.inRange(hsv, lower_skin, upper_skin)

# Apply a Gaussian blur to the mask
mask = cv2.GaussianBlur(mask, (3, 3), 0)

# Perform morphological operations to remove noise and fill in gaps
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)

# Apply the mask to the original image
result = cv2.bitwise_and(img, img, mask=mask)

# Display the results
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Skin Segmentation', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

