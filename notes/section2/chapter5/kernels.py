import cv2
import numpy as np

# cv2.filter2D() is the function used to apply kernels

# example
kernel_averaging_5_5 = np.ones((5, 5), np.float32) / 25

img = cv2.imread('./images/image.jpg')
cv2.imshow('source', img)
cv2.waitKey()
cv2.destroyAllWindows()

smooth_img_f2d = cv2.filter2D(img, -1, kernel_averaging_5_5)
cv2.imshow('filter2d blur', smooth_img_f2d)
cv2.waitKey()
cv2.destroyAllWindows()


# smoothing/bluring images

# cv2 blur does an average of pixel values in a block and replace the center of the block with this average
blur_img = cv2.blur(img, (10, 10)) # the block will be 10x10
cv2.imshow('cv2 blur', blur_img)
cv2.waitKey()
cv2.destroyAllWindows()

# gaussian filtering
gausian_blur_img = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imshow('gausian blur', gausian_blur_img)
cv2.waitKey()
cv2.destroyAllWindows()

# median filtering
# this one in specific will reduce the salt and pepper noise of an image
'''Salt and pepper noise is a type of noise that can occur in digital images.
 It is characterized by the appearance of random black and white pixels scattered
 throughout the image. The black pixels are referred to as "salt" and the white pixels
 are referred to as "pepper", hence the name.'''
median_blur = cv2.medianBlur(img, 9)
cv2.imshow('median blur', median_blur)
cv2.waitKey()
cv2.destroyAllWindows()

# bilateral filtering
# applied to reduce noise while keeping the edges sharp
bilateral_blur = cv2.bilateralFilter(img, 5, 10, 10)
cv2.imshow('bilateral blur', median_blur)
cv2.waitKey()
cv2.destroyAllWindows()


# sharpening images
# one simple aproach is to perform unsharp masking, where an unsharp (smoothed) version of the image is
# subtracted from the original image

smoothed = cv2.GaussianBlur(img, (9, 9), 10)
unsharped = cv2.addWeighted(img, 1.5, smoothed, -1.5, 0)
cv2.imshow('unsharp masking', unsharped)
cv2.waitKey()
cv2.destroyAllWindows()
