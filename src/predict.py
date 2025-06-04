from ultralytics import YOLO

# Load trained model weights
model = YOLO("models/best.pt")  # path to your trained model

# Predict on an image
results = model.predict(
    source="test_image.jpg",  # or a folder
    conf=0.3,
    save=True,
    show=True
)
