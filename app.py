import gradio as gr
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os
import gdown

# ✅ Download model from Google Drive if not present
model_path = "best.pt"
file_id = "1O9C2ACDdqWKbgEShbf3AkuSqBKWDgJ3t"

if not os.path.exists(model_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, model_path, quiet=False)

# ✅ Load the model
model = YOLO(model_path)

# ✅ Prediction function: image + text description
def detect_damage(img):
    results = model.predict(img, conf=0.25)
    annotated = results[0].plot()  # numpy array image

    # Extract class names
    detected_classes = set()
    for box in results[0].boxes:
        cls_id = int(box.cls[0].item())
        cls_name = model.names[cls_id]
        detected_classes.add(cls_name)

    if detected_classes:
        description = "Detected damage: " + ", ".join(detected_classes)
    else:
        description = "No visible damage detected."

    return Image.fromarray(annotated), description

# ✅ Gradio UI
demo = gr.Interface(
    fn=detect_damage,
    inputs=gr.Image(type="pil", label="Upload Car Image"),
    outputs=[
        gr.Image(type="pil", label="Detected Damage"),
        gr.Textbox(label="Damage Description")
    ],
    title="🚗 Car Damage Detector (YOLOv8)",
    description="Upload an image to detect scratches, dents, cracks, and more using a YOLOv8 model trained on 6 damage classes."
)

demo.launch()
