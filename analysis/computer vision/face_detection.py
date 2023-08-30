import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np
import time
model_path='blaze_face_short_range.tflite'

BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
FaceDetectorResult = mp.tasks.vision.FaceDetectorResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a face detector instance with the live stream mode:
def print_result(result: FaceDetectorResult, output_image: mp.Image, timestamp_ms: int):
    print('face detector result: {}'.format(result))

options = FaceDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)

cam=cv2.VideoCapture(0)
with FaceDetector.create_from_options(options) as detector:
    while True:
        status,img=cam.read()
        if not status:
            print('Camera is not available')
            break
        mp_image=mp.Image(image_format=mp.ImageFormat.SRGB,data=img)
        frame_timestamp_ms=int(time.time()*1000)
        detector.detect_async(mp_image,frame_timestamp_ms)
        if cv2.waitKey(1)==27:
            break
    cam.release()
    cv2.destroyAllWindows()
    