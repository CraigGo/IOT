import numpy as np
import cv2
import paho.mqtt.client as mqtt

print ("Running v0.7")

# mqtt specifics
MQTT_HOST="mosquitto"
MQTT_PORT=1883
MQTT_TOPIC="test_topic"

# connection event
def on_connect(client, data, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection: ", str(rc))

# create MQTT client
mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)

face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face detection and other logic goes here
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]
        print("face detected ", face.shape)
        rc,jpg = cv2.imencode('.jpg', face)
        msg = jpg.tobytes()
        mqttclient.publish(MQTT_TOPIC, payload=msg, qos=0, retain=False)

