from ultralytics import YOLO

# Load trained model
model = YOLO("models/best.pt")

# Evaluate on validation or test set
metrics = model.val()  # Will use path in YAML file
print(metrics)
