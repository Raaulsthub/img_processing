import cv2
import numpy as np 
from skimage.filters import threshold_otsu
from skimage import img_as_ubyte

img = cv2.imread('./images/metro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# returns tresh value
thresh = threshold_otsu(gray)
# binary has gray image thresholded in true or false
binary = gray > thresh
# converting from true or false to uint8
binary = img_as_ubyte(binary)

cv2.imshow('thresh sk-image', binary)
cv2.waitKey()
cv2.destroyAllWindows()

# sk also provides techniques such as triangle (simple), niblack(adaptive) and sauvola(adaptive)
# and more