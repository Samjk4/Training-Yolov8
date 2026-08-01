from ultralytics import YOLO
YOLO("best.pt").predict(source='0',show=True)