from ultralytics import YOLO
import cv2
model = YOLO("best.pt")
video = cv2.VideoCapture(0)
if not video.isOpened() :
    print("webcam not opened")
else :
    print("webcam opened successfully")
    colors = {
                0: (0, 0, 255),  # Fire
                1: (255, 0, 0)   # Smoke
            }
    while True :
        success , image = video.read()
        if success: 
           results = model(image, verbose=False)
           fire_count = 0
           smoke_count = 0
           for box in results[0].boxes:
               x1,y1,x2,y2 = box.xyxy[0]
               x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
               confidence = float(box.conf[0])
               if confidence < 0.5:
                   continue 
               class_id = int(box.cls[0])
               class_name = results[0].names[class_id]
               if class_id == 0 :
                   fire_count += 1 
               if class_id == 1 :
                   smoke_count += 1
               color = colors[class_id]
               cv2.rectangle(image,(x1,y1),(x2,y2),color,3)
               cv2.putText(image,f"{class_name} {confidence:.2f}",(x1,y1-10),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1,color=color,thickness = 2,lineType = cv2.LINE_AA)
           cv2.putText(image,f"Fire Count : {fire_count} ",(10, 30),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1,color=(0,0,0),thickness = 2,lineType = cv2.LINE_AA)
           cv2.putText(image,f"Smoke Count : {smoke_count} ",(10, 60),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1,color=(0,0,0),thickness = 2,lineType = cv2.LINE_AA)
           cv2.imshow("detection",image)
           if cv2.waitKey(1) & 0xFF == ord('q'):
              break                    
        else:
            print("No image recieved")
video.release()
cv2.destroyAllWindows()                