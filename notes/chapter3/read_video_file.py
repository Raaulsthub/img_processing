import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('video_path', help='path to the video that will be read', type=str)
args = parser.parse_args()

cap = cv2.VideoCapture(args.video_path)

# loop through the frames in the video
while True:
    # read a frame from the video
    ret, frame = cap.read()

    # if the frame was read successfully
    if ret:
        # display the frame
        cv2.imshow('frame', frame)

        # wait for 25 milliseconds and check if the user pressed the 'q' key
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()

