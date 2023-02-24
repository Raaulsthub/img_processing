import cv2
import numpy as np

# Define a callback function to handle mouse events
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 10, (0, 255, 0), -1)

# Create an empty black image with a size of 512 x 512
img = np.zeros((512, 512, 3), np.uint8)

# Create a window to display the image and set the mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    # Display the image and wait for a key press
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all windows
cv2.destroyAllWindows()