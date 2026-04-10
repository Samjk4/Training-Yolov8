import cv2
from test import detect_crosswalk

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, crosswalk = detect_crosswalk(frame)

    if crosswalk:
        print("🚨 前方有斑馬線")

    cv2.imshow("Crosswalk Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()