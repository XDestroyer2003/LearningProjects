# advance projects
import numpy as np
import cv2

cap = cv2.VideoCapture('3.mp4')
buffer = None
while True:
    _, frame = cap.read()
    if buffer is None:
        buffer = frame[np.newaxis, 0, 0:]
    else:
        buffer = np.row_stack((buffer, frame[np.newaxis, buffer.shape[0]]))

        frame[buffer.shape[0] + 1] = [0, 255, 0]

        frame[:buffer.shape[0]] = buffer
        cv2.imshow('glitch', frame)
        cv2.waitKey(4)
