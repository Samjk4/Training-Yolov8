from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.export(format="tflite", imgsz=320)

print("完成！請去 runs/detect/export/ 找 .tflite")