# Training YOLOv8

這是一個使用 YOLOv8 進行交通物件偵測的專案，支援訓練、測試與模型匯出。

## 專案目標

此專案用於訓練一個交通場景偵測模型，能夠辨識交通相關物件，並支援：

- 訓練交通模型
- 測試已訓練模型
- 將 `.pt` 模型轉換為 `.tflite`
- 使用模型進行影像或影片推論

## 專案結構

```text
test_model/
├── data/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   ├── labels/
│   ├── videos/
│   └── weights/
├── src/
│   ├── train.py
│   ├── test.py
│   ├── export.py
│   └── detect.py
├── README.md
```

## 環境安裝

建議使用 Conda 建立虛擬環境：

```bash
conda create -n yolo8 python=3.10 -y
conda activate yolo8
pip install ultralytics torch==2.1.2 numpy opencv-python pywin32 pyyaml pillow scipy matplotlib tqdm
```

## 資料準備

請先建立資料夾：

```bash
mkdir -p data/images/train data/images/val data/images/test data/labels data/videos data/weights
```

資料集格式建議遵循 YOLO 格式：

- 圖片放在 `data/images/train`、`data/images/val`、`data/images/test`
- 對應標註檔 `.txt` 放在 `data/labels/` 中
- 影片檔可放在 `data/videos/`

## 訓練模型

從專案根目錄執行：

```bash
python src/train.py --data src/data.yaml --epochs 100 --img 640 --batch 64 --device 0
```

常用參數說明：

- `--epochs`：訓練週期
- `--img`：輸入影像大小
- `--batch`：批次大小
- `--device`：運算裝置，可填 `0` 或 `cpu`

訓練完成後，模型權重會輸出到：

```text
runs/train/exp/weights/best.pt
```

## 測試模型

如果你要測試某個模型，建議先把要測試的權重檔複製並命名為 `test.pt`：

### Windows
```powershell
copy runs\train\exp\weights\best.pt runs\train\exp\weights\test.pt
```

### Linux / macOS
```bash
cp runs/train/exp/weights/best.pt runs/train/exp/weights/test.pt
```

然後執行測試：

```bash
python src/test.py --weights runs/train/exp/weights/test.pt --data src/data.yaml --img 640 --conf 0.25 --device 0
```

## 將 `.pt` 轉為 `.tflite`

```bash
python src/export.py --weights runs/train/exp/weights/test.pt --img 640 --include tflite --device 0
```

匯出完成後，模型將可用於行動裝置或邊緣裝置部署。

## 推論 / 偵測

進行影片偵測：

```bash
python src/detect.py --weights runs/train/exp/weights/test.pt --img 640 --source data/videos/video.mp4
```

也可以對單張圖片做偵測：

```bash
python src/detect.py --weights runs/train/exp/weights/test.pt --img 640 --source data/images/test/example.jpg
```

## 輸出結果位置

- 訓練結果：`runs/train/`
- 測試結果：`runs/test/`
- 匯出模型：`runs/export/`

## 備註

- 如果你想使用其他模型名稱，只要把它複製成 `test.pt` 即可。
- 若使用 GPU，建議將 `--device 0` 改成實際可用的 GPU 編號。
- 可依據資料集大小與硬體資源調整 `--epochs`、`--batch`、`--img` 等參數。

