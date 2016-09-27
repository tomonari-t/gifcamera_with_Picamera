import os
import time
import picamera

CAPTURED_NUM = 10
FRAME_PER_SEC = 60
PHOTO_DIR = "./photo/"

def _clearDir():
    for i in os.listdir(PHOTO_DIR):
        if os.path.isfile(os.path.join(PHOTO_DIR, i)):
            os.remove(os.path.join(PHOTO_DIR, i))

def _getFrameNum(sec):
    return sec * FRAME_PER_SEC

def _filenames():
    frame = 0
    while frame < CAPTURED_NUM:
        yield PHOTO_DIR + 'image%02d.jpg' % frame
        frame += 1

def _capture(frameRate):
    with picamera.PiCamera() as camera:
        camera.resolution = (800, 600)
        camera.framerate = frameRate
        try:
            time.sleep(2)
            camera.capture_sequence(_filenames(), use_video_port=True)
            print('Captured')
        finally:
            camera.close()

def captureWithSec(seconds = 1):
    _clearDir()
    frameNum = _getFrameNum(seconds)
    _capture(frameNum / CAPTURED_NUM)
