from ultralytics import YOLO

model = YOLO('yolo11n.pt')

results = model('araba.jpg')
results[0].show()

#object detection