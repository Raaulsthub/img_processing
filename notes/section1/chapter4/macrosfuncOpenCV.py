from matplotlib import pyplot as plt
import cv2
import numpy as np

# color macros for open cv (BGR)

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255), 
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'dark_gray': (50, 50, 50), 'white': (255, 255 ,255),
          'black': (0, 0, 0)}


def draw_with_matplotlib(image):
    # conversion
    image = image[:, :, ::-1]
    plt.imshow(image)
    plt.show()

