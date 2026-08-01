from ultralytics import YOLO

# 載入你訓練好的模型
model = YOLO("runs/detect/custom_yolo-4/weights/best.pt")

# 轉成 TFLite
model.export(format="tflite")