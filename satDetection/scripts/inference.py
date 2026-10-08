#to test with my own image

if __name__ == "__main__":
     from ultralytics import YOLO
     import cv2

#load model with best weights 
print ("loading model with best weights...")

model = YOLO('runs/obb/results/yolov8n_obb_dota/weights/best.pt')

#image path
image_path = 'test_image2.png' #image here

#commence detection
results = model.predict(
 
     source = image_path,
     conf = 0.25, #changeable 
     iou = 0.4,
     imgsz = 1024, 
     save = True,
     project = 'results/inference',
     name = 'run1'

)

#print what was detected
for r in results:
     for box in r.obb:
         cls = int(box.cls)
         conf = float(box.conf)
         print(f"detected class: {model.names[cls]} - confidence: {conf:.2f}")
