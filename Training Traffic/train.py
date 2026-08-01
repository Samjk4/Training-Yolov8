from ultralytics import YOLO

def main():
    # 1. 載入模型（從官方預訓練開始）
    model = YOLO("yolov8n.pt")

    # 2. 開始訓練
    model.train(
        data="dataset/data.yaml",   # 你的資料集
        epochs=50,                 # 訓練次數
        imgsz=640,                # 圖片大小
        batch=8,                # 批次大小（不夠記憶體就改8或4）
        name="custom_yolo",      # 輸出資料夾名稱
        device=0                 # GPU=0 / CPU用 "cpu"
    )

if __name__ == "__main__":
    main()