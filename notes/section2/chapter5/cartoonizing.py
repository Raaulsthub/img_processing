import cv2

# Load the input image
img = cv2.imread('./images/wilson2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply bilateral filtering to the grayscale image
gray_smooth = cv2.bilateralFilter(gray, 11, 17, 17)

# Apply adaptive thresholding to the smoothed image
thresh = cv2.adaptiveThreshold(gray_smooth, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Convert the thresholded image to color
thresh_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

# Apply bitwise and operation to the original image and the thresholded color image
cartoon = cv2.bitwise_and(img, thresh_color)
cartoon_smoothed = cv2.medianBlur(cartoon, 9)

# Display the cartoonized image
cv2.imshow('Cartoonized Image', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./images/cartoon_wilson.jpg', cartoon)

'''Load the input image using the cv2.imread() function. The input image should be in BGR color space.
Convert the image to grayscale using the cv2.cvtColor() function. This simplifies the image and reduces the amount of data that needs to be processed.
Apply a bilateral filter to the grayscale image using the cv2.bilateralFilter() function. The bilateral filter smooths the image while preserving the edges, which is important for the cartoon effect. The parameters d, sigmaColor, and sigmaSpace control the size of the filter and the amount of smoothing.
Apply adaptive thresholding to the smoothed image using the cv2.adaptiveThreshold() function. Adaptive thresholding is used to obtain a binary image where the edges are emphasized. The parameters blockSize and C control the size of the neighborhood and the threshold value.
Apply median blur to the binary image using the cv2.medianBlur() function. This removes small details and smooths the image further.
Apply the bitwise_and operation to the input image and the blurred binary image using the cv2.bitwise_and() function. This combines the two images in such a way that only the edges and regions with high contrast are retained. This creates the cartoon effect.
Save the output image using the cv2.imwrite() function.'''