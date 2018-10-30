from vision import YOLO

def detect_image_web():
    yolo=YOLO()
    result = yolo.detect_image(image)
    return result
