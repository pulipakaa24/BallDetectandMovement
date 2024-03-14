from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov9c.pt')
 
# Training.
results = model.train(
   data='tennis.yaml',
   imgsz=1280,
   epochs=50,
   batch=8,
   workers=0,
   name='yolov9c_8b_50e')