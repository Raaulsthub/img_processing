import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('path_to_image', help='path to input image to be displayed')
args = parser.parse_args()
image = cv2.imread(args.path_to_image)
cv2.imshow('loaded image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()