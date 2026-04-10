from ultralytics import YOLO
YOLO("yolov8n.pt").predict(source='0',show=True)