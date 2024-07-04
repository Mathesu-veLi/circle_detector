import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret: break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_blurred = cv.medianBlur(gray, 5)
    cv.imshow("frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'): break

videoCapture.release()
cv.destroyAllWindows()