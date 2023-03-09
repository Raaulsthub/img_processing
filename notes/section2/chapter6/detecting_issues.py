import numpy as np
import cv2
from matplotlib import pyplot as plt


# if the average value in all pixes of an image is high (ex 255), it means that most pixels
# of the image will very close to white color ,on the contrary if they are low (ex 30)
# it means that most pixels will be very close to black
# this can be seen on the histogram

img = cv2.imread('./images/witcher.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()

# reducing brightness
add_vector = np.ones(img.shape, dtype='uint8') * 40
img = cv2.subtract(img, add_vector)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()