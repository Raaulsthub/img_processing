import cv2
import argparse

# getting camera index
parser = argparse.ArgumentParser()
parser.add_argument('cam_index', help='index of the camera to be read', type=int)
args = parser.parse_args()

# object that reads from camera
capture = cv2.VideoCapture(args.cam_index)

print(f"frame width: {capture.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"frame height: {capture.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f"frames per second: {capture.get(cv2.CAP_PROP_FPS)}")


if capture.isOpened() is False:
    print("Not able to connect to camera")
    exit(-1)

frame_index = 0

while capture.isOpened():
    # capture frame by frame from camera
    ret, frame = capture.read()
    if ret is True:
        cv2.imshow('input frame from camera', frame)

        # saving frames if we press c
        # cv2 wait key is bitwise and operating it with 0XFF makes only the last 8 bits remain
        if cv2.waitKey(20) & 0XFF == ord('c'):
            frame_name = 'camera_frame){}.png'.format(frame_index)
            cv2.imwrite('images/' + frame_name, frame)
            frame_index += 1
        
        # press q to exit the program
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    else:
        break

capture.release()
cv2.destroyAllWindows()
