import cv2

CAM_IDX=0
cam=cv2.VideoCapture(CAM_IDX)
while cam.isOpened():
    state,frame=cam.read()
    if not state:
        print('Cannot open webcam')
        break
    frame=cv2.flip(frame,1)
    
    print(state,frame.shape)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(10)==27:
        break
cam.release()
cv2.destroyAllWindows()