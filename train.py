from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='tennis.yaml',
   imgsz=1280,
   epochs=50,
   batch=32,
   workers=0,
   name='yolov8n_32b_50e')