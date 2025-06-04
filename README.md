# 🚗 Car Damage Detection using YOLOv8

An AI-powered system that detects car damages like dents, scratches, and cracks from images using YOLOv8. This project automates the inspection process for insurance claims, resale evaluation, and repairs, providing a fast and user-friendly tool for both technical and non-technical users.

---

## 📌 Problem Statement

Manual car damage inspection is slow, inconsistent, and subjective. There's a need for a reliable AI-based solution that can visually detect and classify damage types from car images — ideal for car owners, insurance agents, and vehicle inspectors.

---

## 🧠 Solution Overview

We used **YOLOv8**, a state-of-the-art object detection model, to detect various types of car damage:

- 🔧 Dents  
- 🪓 Scratches  
- 🔩 Cracks  
- 🚗 Other visual damages

---

## 📂 Dataset

- **Name**: CarDD  
- **Size**: 1,000+ annotated car images  
- **Classes**: Scratch, Dent, Crack, etc.  
- **Preprocessing**: Resizing, label formatting, train-validation split

---

## ⚙️ Model & Training

- **Model**: YOLOv8
- **Epochs**: 150  
- **Advantages**:
  - Lightweight and fast
  - Optimized for real-time detection
  - Easy deployment in web apps

- **Performance**:
  - **Precision**: 76%
  - **Recall**: 67%
  - **mAP@0.5**: 72.3%
  - **mAP@0.95**: 57.4%

---

## 🚀 Deployment

- **Interface**: Gradio
- **Hosting**: Hugging Face Spaces  
- **Live Demo**: [Click to Try](https://huggingface.co/spaces/umerforsure/Car_Damage_Detection)

---

## 📁 Project Structure

```
Car-Damage-Detection/
│
├── dataset/             # Dataset info or sample images
├── models/              # Trained weights or link
├── src/                 # Training & inference scripts
│   ├── train.py
│   └── predict.py
├── app.py               # Gradio web interface
├── requirements.txt     # Python dependencies
├── README.md
└── LICENSE
```

---

## 🧪 How to Run Locally

```bash
# Clone repo
git clone https://github.com/your-username/Car-Damage-Detection.git
cd Car-Damage-Detection

# Install dependencies
pip install -r requirements.txt

# Run Gradio app
python app.py
```

---

## 📎 Links

- 📊 **Results & Epochs Folder**: [Google Drive](https://drive.google.com/drive/u/0/folders/1GdiSe2gcHjo6hzYV0uDFW38dmkZm4bd2)
- 🖼️ **Dataset**: [CarDD Project Site](https://cardd-ustc.github.io)
- 📑 **Final Slides**: [Google Slides](https://docs.google.com/presentation/d/1sVJkVlp1rgZvmqmWY7Rjk2-STBHoDQNz8UXCDJ_yEOU/edit)
- ⚙️ **Code**:[Colab Sheet](https://colab.research.google.com/drive/1gHfJKPl7vTjHNy3Jd6_qXmodOk9IdQUO#scrollTo=ybVeyTBhAJI3) 
---

## 📄 License

This project is licensed under the MIT License.
