# 🔥 Fire & Smoke Detection using YOLOv8

A real-time **Fire & Smoke Detection System** built using **YOLOv8**, **OpenCV**, and **Python**. The model can detect fire and smoke in images, videos, and live webcam streams while displaying bounding boxes, confidence scores, and object counts.

---

## 🚀 Features

- 🔥 Fire Detection
- 💨 Smoke Detection
- 🖼️ Image Detection
- 🎥 Video Detection
- 📷 Live Webcam Detection
- 📦 Bounding Boxes
- 📊 Confidence Scores
- 🔢 Fire & Smoke Count
- 💾 Save Annotated Images
- 💾 Save Annotated Videos
- ⚡ Real-time Inference

---

## 🛠️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- NumPy

---

## 📂 Project Structure

```
Fire-Smoke-Detection/
│
├── detect_image.py
├── detect_video.py
├── detect_webcam.py
├── best.pt
├── requirements.txt
├── README.md
│
├── images/
│   └── input_image.png
│
├── videos/
│   └── input_video.mp4
│
├── outputs/
│   ├── output.jpg
│   └── output_video.mp4
│
└── assets/
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Fire-Smoke-Detection.git
```

Move into the project directory:

```bash
cd Fire-Smoke-Detection
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Image Detection

```bash
python detect_image.py
```

---

### Video Detection

```bash
python detect_video.py
```

---

### Webcam Detection

```bash
python detect_webcam.py
```

---

## 📊 Model Information

- Model: YOLOv8 Nano
- Framework: Ultralytics YOLOv8
- Classes:
  - Fire
  - Smoke

---

## 📈 Training Performance

| Metric | Score |
|--------|------:|
| Precision | 94.7% |
| Recall | 93.8% |
| mAP@50 | 97.5% |
| mAP@50-95 | 62.4% |

---

## ✨ Outputs

The system provides:

- Bounding boxes around detected objects
- Confidence score for each detection
- Fire count
- Smoke count
- Saved output images
- Saved output videos
- Live webcam detection

---

## 🔮 Future Improvements

- Object Tracking
- Fire Alarm System
- Email/SMS Alerts
- Streamlit Web Application
- Flask API Deployment
- Edge Device Deployment

---

## 👨‍💻 Author

**Dhairya Nagpal**

- LinkedIn: https://www.linkedin.com/in/dhairya-nagpal7
- GitHub: https://github.com/Dhairya1000
