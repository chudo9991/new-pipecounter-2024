from ultralytics import YOLO
from roboflow import Roboflow
import os

rf = Roboflow(api_key="YeSDO8WIgLLUodg0NjBt")
project = rf.workspace("project-sdhb2").project("pipes-v2")
version = project.version(2)
dataset = version.download("yolov11")

# Load a pretrained model (recommended for training)
model = YOLO("yolo11n.pt")

# Get the correct path to data.yaml
data_yaml_path = os.path.join(dataset.location, "data.yaml")

# Train the model
results = model.train(data=data_yaml_path,
                      epochs=100, imgsz=640, task="detect")

# Save the model
model.save("yolov11n_pipes.pt")
