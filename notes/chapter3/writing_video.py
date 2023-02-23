import time
import cv2
import argparse

# getting camera index
parser = argparse.ArgumentParser()
parser.add_argument('cam_index', help='index of the camera to be read', type=int)
parser.add_argument('video_output_path', help='path to the video output', type=str)
args = parser.parse_args()

# object that reads from camera
capture = cv2.VideoCapture(args.cam_index)

if capture.isOpened() is False:
    print("Not able to connect to camera")
    exit(-1)

frame_index = 0

# getting some camera properties
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# defining video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# video writer, in case the last argument were true, the video would be written in colors, false means gray scale
out_gray = cv2.VideoWriter(args.video_output_path, fourcc, int(fps), (int(frame_width), int(frame_height)), False)

while capture.isOpened():
    # capture frame by frame from camera
    ret, frame = capture.read()
    if ret is True:
        processing_start = time.time()
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        out_gray.write(gray_frame)
        

        # fps calculum
        processing_end = time.time()
        processing_time_frame = processing_end - processing_start
        fps = 1 / processing_time_frame
        print(f'fps: {fps}')

        # showing image
        cv2.imshow('video', gray_frame)
        # press q to exit the program
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out_gray.release()
cv2.destroyAllWindows()