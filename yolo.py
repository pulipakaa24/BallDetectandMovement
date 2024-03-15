from ultralytics import YOLO

model = YOLO("runs/detect/yolov8m_16b_50e_smallset/weights/best.pt")

results = model.predict(source='0', show=True)

print(results)
