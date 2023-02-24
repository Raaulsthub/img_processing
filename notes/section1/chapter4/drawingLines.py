import cv2
import macrosfuncOpenCV as macros
import numpy as np

# creating black 500x500 colored image
image = np.zeros((500, 500, 3), dtype='uint8')

# turning it to dark gray
image[:] = macros.colors['blue']

# painting some lines
separation = 40
for key in macros.colors:
    cv2.line(image, (0, separation), (500, separation), macros.colors[key], 10)
    separation += 40

cv2.imshow('drawing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

macros.draw_with_matplotlib(image)