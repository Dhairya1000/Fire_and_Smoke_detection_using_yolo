from ultralytics import YOLO
import cv2
import time
import pyttsx3
import pygame
import csv
from datetime import datetime
import threading
import os 
import requests
from dotenv import load_dotenv

load_dotenv()

ALERT_FOLDER = "alerts" 
os.makedirs(ALERT_FOLDER, exist_ok=True)

speech_lock = threading.Lock()

model = YOLO("best.pt")
def speak(message):
    with speech_lock:
        engine.say(message)
        engine.runAndWait()
engine = pyttsx3.init()

engine.setProperty("rate", 170)   # Speaking speed

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_alert(message, frame):

    image_path = os.path.join(ALERT_FOLDER,f"fire_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")

    # Save current frame
    cv2.imwrite(image_path, frame)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    with open(image_path, "rb") as photo:

        requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "caption": message
            },
            files={
                "photo": photo
            }
        )

last_fire_alert = 0
last_smoke_alert = 0

ALERT_DELAY = 10      # seconds
video = cv2.VideoCapture(0)

# Initialize previous time
prev = time.time()

pygame.mixer.init()
pygame.mixer.music.load("alarm_sound.mp3")
alarm_playing = False

if not os.path.exists('result.csv'):
                        header = ['Time','Class','Confidence']
                        with open ('result.csv',mode='a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow(header)

fire_frames = 0
no_fire_frames = 0

if not video.isOpened():
    print("Webcam not opened")
else:
    print("Webcam opened successfully")

    colors = {
        0: (0, 0, 255),    # Fire
        1: (255, 0, 0)     # Smoke
    }

    while True:
        success, frame = video.read()

        if success:

            results = model(frame, verbose=False)

            fire_count = 0
            smoke_count = 0
            max_fire_confidence = 0

            for box in results[0].boxes:

                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

                confidence = float(box.conf[0])

                if confidence < 0.5:
                    continue

                class_id = int(box.cls[0])
                class_name = results[0].names[class_id]
                
                if class_id == 0:
                    fire_count += 1
                else:
                    smoke_count += 1  

                color = colors[class_id]
                
                current_confidence = confidence 

                if class_id == 0:
                    if current_confidence > max_fire_confidence:
                        max_fire_confidence = current_confidence

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

                cv2.putText(
                    frame,
                    f"{class_name} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    color,
                    2
                ) 

            current_time = time.time()

            # Fire Alert
            if fire_count > 0:
                if current_time - last_fire_alert > ALERT_DELAY:

                    threading.Thread(
                        target=speak,
                        args=("Warning! Fire detected. Please evacuate immediately.",),
                        daemon=True
                    ).start()

                    last_fire_alert = current_time

                # Smoke Alert
            elif smoke_count > 0:
                if current_time - last_smoke_alert > ALERT_DELAY:
                    threading.Thread(
                        target=speak,
                        args=("Warning! Smoke detected.",),
                        daemon=True
                    ).start()

                    last_smoke_alert = current_time
                    
            # Count consecutive fire frames
            if fire_count > 0:
                fire_frames += 1
                no_fire_frames = 0
            else:
                fire_frames = 0
                no_fire_frames += 1

            if fire_frames >= 6 and not alarm_playing:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if os.path.exists('result.csv'):
                        data = [now,'Fire',round(max_fire_confidence,2)]
                        with open ('result.csv',mode='a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow(data)
                    pygame.mixer.music.play(-1)
                    alarm_playing = True

                    message = f"""
🚨 FIRE ALERT 🚨

📅 Time: {now}
🎯 Confidence: {max_fire_confidence:.2f}
🔥 Fire Count: {fire_count}

Please inspect the area immediately.
"""
                    
                    threading.Thread(
                        target=send_telegram_alert,
                        args=(message, frame.copy()),
                        daemon=True
                    ).start()
                    
                
            if alarm_playing:
                cv2.rectangle(frame, (0, frame.shape[0]-50), (frame.shape[1],frame.shape[0]), (0, 0, 255), -1)

                cv2.putText(
                    frame,
                    "WARNING: FIRE DETECTED",
                    (85, frame.shape[0] - 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2
                )
                    
            if no_fire_frames >= 30 and alarm_playing:
                    pygame.mixer.music.stop()
                    alarm_playing = False
                    fire_frames = 0

            # for black bg 
            cv2.rectangle(frame,(5,5),(250,110),(0,0,0),-1)

            # Count display
            cv2.putText(frame, f"Fire Count : {fire_count}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255), 2)

            cv2.putText(frame, f"Smoke Count : {smoke_count}",
                        (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 0, 0), 2)

            # FPS Calculation
            curr = time.time()
            fps = 1 / (curr - prev)
            prev = curr

            cv2.putText(frame,
                        f"FPS : {fps:.2f}",
                        (10, 90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 0),
                        2)

            cv2.imshow("Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            print("No image received")
            break

video.release()
cv2.destroyAllWindows()
pygame.mixer.quit()