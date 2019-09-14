import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    if frame is None:
        print("Error: No Image")
        break
    if frame.size > 2:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #gray = frame

# face detection and other logic goes here

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]
        print("face detected ", face.shape, face.dtype)
        # msg = face.tobytes()
        rc,jpg = cv2.imencode('.png', face)
        msg = jpg.tobytes()
        mqttclient.publish(MQTT_TOPIC, payload=msg, qos=0, retrain=False)
        # cv2.imshow('face', face)
        # cv2.waitKey(0)

# cv2.destroyAllWindows()
