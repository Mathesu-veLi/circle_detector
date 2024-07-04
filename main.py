import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret: break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_blurred = cv.GaussianBlur(gray, (17,17), 0)
    circles = cv.HoughCircles(gray_blurred, 
                               cv.HOUGH_GRADIENT, dp=1.2, minDist=100,
                               param1=100, param2=30, minRadius=30, maxRadius=100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv.circle(frame, (x, y), 1, (0, 100, 100), 3)
            cv.circle(frame, (x, y), r, (255, 0, 255), 3)
    
    cv.imshow("frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'): break

videoCapture.release()
cv.destroyAllWindows()