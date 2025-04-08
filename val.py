from ultralytics import YOLO

# Load a model
model = YOLO("root/autodl-tmp/UAVD-Mamba/UAVD-Mamba/weights/best.pt") 

# Validate the model
metrics = model.val(data=r'root/autodl-tmp/UAVD-Mamba/UAVD-Mamba/datasets/single.yaml',batch =8 ) 
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list contains map50-95 of each category