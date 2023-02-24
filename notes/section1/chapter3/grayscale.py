import cv2
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('input_image_path', help='path to the image to be processed')
parse.add_argument('output_image_path', help='path where the image should be saved')
args = parse.parse_args()

img = cv2.imread(args.input_image_path)
cv2.imshow('raw image', img)

# convert to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray_img)

# convert to black and white
(thresh, blackAndWhiteImage) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)


cv2.imwrite(args.output_image_path, blackAndWhiteImage)

cv2.waitKey(0)
cv2.destroyAllWindows()