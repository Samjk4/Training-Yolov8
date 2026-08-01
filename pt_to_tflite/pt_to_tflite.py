from ultralytics import YOLO

# 1️⃣ 載入模型（請改成你的實際路徑）
model = YOLO(r"E:\Final project test\model\pt_to_tflite\best.pt")

model.export(
    format="tflite",
    imgsz=640,
)