import jetson_inference
import jetson_utils

net = jetson_inference.detectNet(argv=['--model=onnx/tennis13.onnx', '--labels=onnx/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'], threshold=0.2)

camera = jetson_utils.gstCamera(1280, 960, "dev/video0")

display = jetson_utils.glDisplay()
