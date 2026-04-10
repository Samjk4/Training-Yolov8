import cv2
import numpy as np

def detect_crosswalk(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 增強對比
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 邊緣偵測
    edges = cv2.Canny(blur, 50, 150)

    # 找白色長條結構（斑馬線特徵）
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=2)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    crosswalk_detected = False

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # 過濾太小雜訊
        if area > 5000:
            x, y, w, h = cv2.boundingRect(cnt)

            aspect_ratio = w / float(h)

            # 斑馬線特徵：寬、橫向延伸
            if aspect_ratio > 2:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "Crosswalk", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                crosswalk_detected = True

    return frame, crosswalk_detected

