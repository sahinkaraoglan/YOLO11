from ultralytics import YOLO

model = YOLO('yolo11n.pt')

results = model('0', save=True)

#object detection with webcam