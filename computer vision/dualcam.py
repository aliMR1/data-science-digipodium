import cv2
import numpy as np

cam1=cv2.VideoCapture(0)
cv2.namedWindow('camera 1')
cv2.createTrackbar('minimum','camera 1',0,255,lambda x: None)
cv2.createTrackbar('maximum','camera 1',0,255,lambda x: None)
bs= cv2.createBackgroundSubtractorKNN()
while True:
    st1,img1=cam1.read()
    min= cv2.getTrackbarPos('minimum','camera 1')
    max= cv2.getTrackbarPos('maximum','camera 1')
    outline=cv2.Canny(img1,min,max,3)
    inverted=cv2.bitwise_not(outline)
    cv2.imshow('camera 1',outline)
    mask= bs.apply(img1)
    fg=cv2.bitwise_and(img1,img1,mask=mask)
    cv2.imshow('mask',mask)
    cv2.imshow('fg',fg)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cam1.release()
cv2.destroyAllWindows()