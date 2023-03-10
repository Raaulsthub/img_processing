import numpy as np
import cv2

img = cv2.imread('./images/metro.jpg')
cv2.imshow('colored image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# the following produces the same result as if
# the 3 channels were splitted and then the
# thresholding was applied to each one of them,
# than merging it together

ret1, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('binary threshold', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
