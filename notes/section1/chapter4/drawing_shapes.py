import cv2
import macrosfuncOpenCV as mf
import numpy as np

image = np.zeros((400, 400, 3), dtype='uint8')
image[:] = mf.colors['white']

#           STANDART SHAPES

# COMUM PARAMETERS IN CV2 DRAWING FUNCTIONS
# img - image where the draw will be made
# color - color of the drawing
# thickness - thickness of the shape outline
# linetype - type of shape boundary
    # cv2.LINE_4 - four connected lines
    # cv2.LINE_8 - eight connected lines
    # cv2.LINE_AA - antialiased line - this one is the one with better quality but is slow
# shift - indicates the number of fractional bits in connection with the coordinates of some points defining the shape

# draw a line (image, point1, point2, color, thickness, linetype, shift)
cv2.line(image, (0, 0), (400, 400), mf.colors['magenta'], 2, lineType=cv2.LINE_AA, shift=0)

# draw a rectangle (image, point 1, point 2, color, thickness, lineType, shift), thickness -1 means filled
cv2.rectangle(image, (0, 0), (200, 200), mf.colors['blue'], -1, lineType=cv2.LINE_8, shift=0)

# draw a circle (image, center, radius, color, thickness, linetype, shift)
cv2.circle(image, (300, 300), 100, mf.colors['black'], 3, lineType=cv2.LINE_AA)

# mf.draw_with_matplotlib(image)



#           ADVANCED SHAPES

# drawing a clip line (limiting line)
# retval, pt1, pt2 = clipLine (imgRect, pt1, pt2)
# if the retval is true, it means that the original pt1 and/or pt2 are inside the rectangle
# if the retval is false, it means that the original points are both outside the rectangle
# the pt1 and pt2 returned, are clipped(limited) to the rectangle

image2 = np.zeros((400, 400, 3), dtype='uint8')
image2[:] = mf.colors['dark_gray']

cv2.line(image2, (0, 0), (300, 300), mf.colors['green'], 3)
cv2.rectangle(image2, (0, 0), (100, 100), mf.colors['blue'], 3)
ret, pt1, pt2 = cv2.clipLine((0, 0, 100, 100), (0, 0), (300, 300))
if ret:
    cv2.line(image2, pt1, pt2, mf.colors['yellow'], 3)


# drawing arrows - cv.arrowedLine(img, p1, p2, color, thickness, lineType, shift, tipLenght)
cv2.arrowedLine(image2, (300, 300), (350, 300), mf.colors['black'], 3, 8, 0, 0.1) # 0.1 means 10% of the line (p1 to p2)

# drawing elipses - cv2.elipse(img, center, axes, angle, startAngle, endAngle, color, thickness, linetype, shift)
cv2.ellipse(image, (80, 80), (60, 40), 0, 0, 360, mf.colors['red'], -1)

# drawing polygones cv2.polylines(img, pts, isClosed, color, thickness, linetype, shift)
# the shape should be (number_vertex, 1, 2)
# triangle
pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
pts = pts.reshape((-1, 1, 2)) # reshaping to number_vertex, 1, 2
cv2.polylines(image2, [pts], True, mf.colors['green'], 3)

# mf.draw_with_matplotlib(image2)

#               TEXT

image3 = np.zeros((400, 400, 3), dtype='uint8')
image3[:] = mf.colors['magenta']

# cv.putText(img, text, org, fontFace, fontScale, color, thickness, linetype, bottomLeftOrigin)
cv2.putText(image3, 'Mastering OpenCV', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.9, mf.colors['white'], 2, cv2.LINE_AA)

mf.draw_with_matplotlib(image3)
