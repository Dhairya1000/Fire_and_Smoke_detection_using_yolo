# 🔥 AI Fire & Smoke Surveillance System using YOLOv8

A real-time Fire and Smoke Detection System built using **YOLOv8**, **OpenCV**, and **Python**. The application detects fire and smoke from webcam or video streams, generates instant voice and alarm alerts, logs detection events, and sends Telegram notifications with captured screenshots.

---

## 🚀 Features

- 🔥 Real-time Fire Detection
- 💨 Smoke Detection
- 🎥 Webcam & Video Support
- 📦 YOLOv8 Object Detection
- 📢 Voice Alert using pyttsx3
- 🚨 Alarm Sound using Pygame
- 📱 Telegram Alert with Screenshot
- 📸 Automatic Screenshot Capture
- 📝 CSV Event Logging
- 📊 Real-time FPS Display
- 🎯 Confidence Score Display
- 🖥️ Bounding Box Visualization

---

## 🛠️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- Pygame
- pyttsx3
- Telegram Bot API
- Requests

---

## 📂 Project Structure

```
Fire-Smoke-Detection/
│
├── best.pt
├── detect.py
├── requirements.txt
├── alarm_sound.mp3
├── result.csv
├── .env.example
├── README.md
│
├── alerts/
│   ├── fire_20260714_101523.jpg
│   └── fire_20260714_111021.jpg
│
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fire-smoke-detection.git

cd fire-smoke-detection
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file

```
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
```

Never upload your real `.env` file.

---

## ▶️ Run

```bash
python detect.py
```

---

## 📱 Telegram Alert

When fire is detected, the system automatically:

- Sends an alert message
- Captures the detection frame
- Sends the screenshot to Telegram

---

## 📸 Screenshots

### Detection

<img width="346" height="252" alt="image" src="https://github.com/user-attachments/assets/b6c54c12-b1ff-410e-9c25-43ebe4528424" />


---

### Telegram Alert

<img width="285" height="136" alt="image" src="https://github.com/user-attachments/assets/fa50941a-c09a-434f-8f84-4e7a14f46190" />

---

## 📌 Future Improvements

- FastAPI Inference API
- Docker Support
- Image Upload Interface
- Video Upload Interface
- Multi-camera Detection
- Email Notifications
- Cloud Deployment

---

## 👨‍💻 Author

**Dhairya**

B.Tech Computer Science (AI & ML)

- LinkedIn: https://www.linkedin.com/in/dhairya-nagpal7
- GitHub: https://github.com/Dhairya1000
