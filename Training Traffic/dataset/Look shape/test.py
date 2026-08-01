import cv2

# 🔧 設定你的檔案
image_path = r"E:\Final project test\model\Training Traffic\dataset\test.jpg"
label_path = r"E:\Final project test\model\Training Traffic\dataset\test.txt"

# class名稱（照你的改）
class_names = ["green", "red", "traffic", "yellow"]

# 讀圖片
img = cv2.imread(image_path)
h, w, _ = img.shape

# 讀 label
with open(label_path, "r") as f:
    lines = f.readlines()

for line in lines:
    data = line.strip().split()

    cls = int(data[0])
    x = float(data[1])
    y = float(data[2])
    bw = float(data[3])
    bh = float(data[4])

    # 🔥 轉成 pixel
    x1 = int((x - bw/2) * w)
    y1 = int((y - bh/2) * h)
    x2 = int((x + bw/2) * w)
    y2 = int((y + bh/2) * h)

    # 畫框
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 顯示文字
    label = class_names[cls]
    cv2.putText(img, label, (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

# 顯示
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()