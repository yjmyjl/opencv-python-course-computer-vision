import cv2

# read webcam
webcam = cv2.VideoCapture(0) # 0 denote webcam number

# visualize webcam

while True:         # forever
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): # when pressed "q" window closes
        break

webcam.release()     # releases allocated memory
cv2.destroyAllWindows()
