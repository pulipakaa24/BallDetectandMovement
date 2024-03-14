from ultralytics import YOLO

model = YOLO("runs/detect/yolov8m_custom7/weights/best.pt")

results = model.predict(source='0', show=True)

print(results)