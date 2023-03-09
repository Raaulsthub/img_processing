import numpy as np
import cv2
from matplotlib import pyplot as plt

# equalizing the histogram will normalize the brightness and 
# also increase the contrast of an image

img = cv2.imread('./images/person.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_img_eq = cv2.equalizeHist(gray_img)

cv2.imshow('gray', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()

# histogram
hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv2.imshow('gray equalized', gray_img_eq)
cv2.waitKey()
cv2.destroyAllWindows()
hist_eq = cv2.calcHist([gray_img_eq], [0], None, [256], [0, 256])
plt.plot(hist_eq)
plt.show()

# normaly the same image, with various levels of brighness will aways have
# a very similar equalized histogram


# color histogram equalization
# the bgb had additive problems and equalization using it will 
# often create new colors and make the image weird
# to equalize we will change the color space to one containing
# a luminance/intensity chanell (yuv, lab, hsv, hsl)

def equalize_color_hsv(img):
    H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    eq_v = cv2.equalizeHist(V)
    return cv2.cvtColor(cv2.merge([H, S, eq_v]), cv2.COLOR_HSV2BGR)

eq_img = equalize_color_hsv(img)
cv2.imshow('equalized color image', eq_img)
cv2.waitKey()
cv2.destroyAllWindows()


# constrast limited adaptive histogram equalization
# it improves the constrast in a way noise cant affect
# its a good algorythm to better contrast
# the problem with histEqualization is that it amplifies noise, and clahe
# tackles that by limiting the contrast amplification

# gray scale
# cliplimit controls contrast amplification limit
clahe = cv2.createCLAHE(clipLimit=2.0)
gray_img_clahe = clahe.apply(gray_img)
cv2.imshow('gray', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('clahe', gray_img_clahe)
cv2.waitKey()
cv2.destroyAllWindows()

# as we can see its way better then normal hist equalization

# for colored images, it follows the logic, convert to a brightness based color space
# apply it only on brightness

def equalize_color_hsv_clahe(img):
    H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    clahe = cv2.createCLAHE(clipLimit=5.0)
    eq_v = clahe.apply(V)
    return cv2.cvtColor(cv2.merge([H, S, eq_v]), cv2.COLOR_HSV2BGR)

eq_img = equalize_color_hsv_clahe(img)
cv2.imshow('equalized color image', eq_img)
cv2.waitKey()
cv2.destroyAllWindows()