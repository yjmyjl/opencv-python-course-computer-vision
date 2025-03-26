import os

import cv2


# read video
video_path = os.path.join('.', 'data', 'monkey.mp4')

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read()    #ret is true if "frame" reads successfully from video

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)           # 40 is 40 miliseconds which is 1/(FPS of video) , her 25fps

video.release()
cv2.destroyAllWindows()
