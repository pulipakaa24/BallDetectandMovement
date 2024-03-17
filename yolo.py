from ultralytics import YOLO

model = YOLO("runs/detect/yolov8yaml_16b_50e/weights/best.pt")

results = model.predict(source='0', show=True)

print(results)
