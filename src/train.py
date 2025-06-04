from ultralytics import YOLO

# Load YOLOv8 model architecture (Nano version)
model = YOLO('yolov8n.yaml')  # or 'yolov8n.pt' if using pretrained weights

# Train model on your custom dataset
model.train(
    data='CarDD_6class_dataset.yaml',  # path to dataset YAML
    epochs=150,
    imgsz=640,
    batch=16,
    name='car_damage_yolov8'
)
