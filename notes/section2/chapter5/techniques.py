import cv2
import numpy as np


# raw image
img = cv2.imread('./images/wilson.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# image blending is image addition but with different weights
# as an example we use the sobel operator, witch is mainly
# used for edge detection, creates an image emphasizing the edges

gradient_x = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0, 3)
gradient_y = cv2.Sobel(gray_img, cv2.CV_16S, 0, 1, 3)

# conversion to uint8
abs_gradient_x = cv2.convertScaleAbs(gradient_x)
abs_gradient_y = cv2.convertScaleAbs(gradient_y)

# combine two images
sobel_img = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)


cv2.imshow('abs_x', abs_gradient_x)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('abs_y', abs_gradient_y)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('sobel_image', sobel_img)
cv2.waitKey()
cv2.destroyAllWindows()


# bitwise operations
lady = cv2.imread('./images/lady.png')
logo = cv2.imread('./images/logo.png')

print(logo.shape)
print(lady.shape)

bitwise_and = cv2.bitwise_and(lady, logo)
cv2.imshow('and', bitwise_and)
cv2.waitKey()
cv2.destroyAllWindows()


bitwise_or = cv2.bitwise_or(lady, logo)
cv2.imshow('or', bitwise_or)
cv2.waitKey()
cv2.destroyAllWindows()

# morphological transformations
raw = cv2.imread('./images/logo.png')
gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
ret, binary_img = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('binary image', binary_img)
cv2.waitKey()
cv2.destroyAllWindows()

# dilation - expanding object boundaries in image, the holes in the object will shrink, it's
# foreground areas will become larger
kernel = np.ones((5, 5), np.uint8) # kernel for dilation
dilatation = cv2.dilate(binary_img, kernel, iterations=1)
cv2.imshow('dilation', dilatation)
cv2.waitKey()
cv2.destroyAllWindows()

# erosion - oposite effect of dilation
erosion = cv2.erode(binary_img, kernel, iterations=5)
cv2.imshow('erosion', erosion)
cv2.waitKey()
cv2.destroyAllWindows()

# the two above were the main ones, under this, all the operations will be derivated from erosion and dilation

# opening operation
# performs erosion followed by a dilation using the same kernel, witch eliminates small groups of undesired pixes(erosion)
# such as salt and pepper noise, and then reducing the undesired effects of erosion by performing dilation
opening = cv2.erode(binary_img, kernel, iterations=1)
opening = cv2.dilate(binary_img, kernel, iterations=1)
cv2.imshow('opening', opening)
cv2.waitKey()
cv2.destroyAllWindows()

# closing operation
# the closing operator uses first dilation than erosion
# the dilation fills small holes n images, but it also make small groups of undesirable pixels bigger,
# erosion is used to rever that
closing = cv2.dilate(binary_img, kernel, iterations=1)
closing = cv2.erode(binary_img, kernel, iterations=1)
cv2.imshow('closing', closing)
cv2.waitKey()
cv2.destroyAllWindows()

# morphological gradient operation - the difference between the dilation an erosion in an image
morph_grad = cv2.morphologyEx(binary_img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('morphgrad', morph_grad)
cv2.waitKey()
cv2.destroyAllWindows()

# top hat operation - the difference between the input image and its opening image
top_hat = cv2.morphologyEx(binary_img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', top_hat)
cv2.waitKey()
cv2.destroyAllWindows()

# black hat operation
# defined as the difference between the input image and it's closing operation image
black_hat = cv2.morphologyEx(binary_img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat', black_hat)
cv2.waitKey()
cv2.destroyAllWindows()



# GENERATING KERNEL FOR MORPHOLOGIC OPERATIONS

# Define the size of the structuring element
kernel_size = (3, 3)

# Create a rectangular structuring element using cv2.getStructuringElement()
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

# Display the structuring element
print(rect_kernel)

cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)

print(cross_kernel)