# 🧠 AI Navigation System for Visually Impaired (YOLO-based)

## 📌 Project Overview

This project develops a **real-time AI navigation assistance system** designed for visually impaired users.
The system uses **YOLOv8 object detection** to identify important environmental elements such as stairs, sidewalks, and traffic lights, and provides **visual + voice guidance**.

---

## 🎯 Features

* 🚶‍♂️ **Downstair Detection**
* 🧭 **Upstair Detection**
* 🚦 **Traffic Light Recognition (Red / Yellow / Green)**
* 🛣 **Sidewalk Detection**
* ⚠️ **Real-time Object Detection**
* 🔊 **Voice Guidance (planned / optional)**

---

## 🏷️ Detection Classes

| Class ID | Label        |
| -------- | ------------ |
| 0        | downstair    |
| 1        | red_light    |
| 2        | yellow_light |
| 3        | green_light  |
| 4        | upstair      |
| 5        | sidewalk     |

---

## 🧱 Project Structure

```
dataset/
 ├── train/
 │    ├── images/
 │    └── labels/
 ├── valid/
 │    ├── images/
 │    └── labels/
 └── data.yaml

train.py
```

---

## ⚙️ Environment Setup

```bash
pip install ultralytics
```

---

## 🚀 Training

Run the training script:

```bash
python train.py
```

### Training Configuration

* Model: YOLOv8n
* Image size: 640
* Batch size: 8
* Epochs: 50
* Device: GPU (CUDA)

---

## 🧪 Inference (Testing)

```python
from ultralytics import YOLO

model = YOLO("runs/detect/custom_yolo/weights/best.pt")
results = model.predict(source="test.jpg", show=True)
```

---

## 📱 Android Deployment (Planned / In Progress)

* Convert `.pt` → `.tflite`
* Use **CameraX** for real-time camera feed
* Run inference on-device (no cloud)
* Add **Text-to-Speech (TTS)** for navigation guidance

---

## ⚠️ Known Issues

* Traffic light detection may be less accurate due to:

  * Small object size
  * Limited training data
* Class imbalance can affect prediction accuracy

---

## 🔧 Future Improvements

* Increase dataset size (especially traffic lights)
* Use YOLOv8-seg for better path detection
* Split model into:

  * Road detection model
  * Traffic light model
* Add obstacle avoidance logic
* Improve voice navigation system

---

## 📊 Technologies Used

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* PyTorch
* Android (planned)

---

## 👤 Author

* Name: Dong Shi Rong
* Project: AI Navigation for the Visually Impaired

---

## 📜 License

This project is for educational and research purposes.
