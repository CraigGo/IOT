import paho.mqtt.client as mqtt

print ("Running v0.6")

# mqtt specifics
MQTT_HOST="mosquitto"
MQTT_PORT=1883
MQTT_TOPIC="test_topic"

# connection event
def on_connect(client, data, flags, rc):
    if rc==0:
        client.subscribe(MQTT_TOPIC, 0)
        print("connected OK")
    else:
        print("Bad connection: ", str(rc))

# subscription event
def on_subscribe(client, userdata, mid, gqos):
    print("Subscribed: ",  str(mid))

# received message event
def on_message(client, obj, msg):
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    print("Msg received")
    f = open("Face.png", 'w')
    f.write(msg.payload)
    f.close()

# create MQTT client
client = mqtt.Client(None, clean_session=True)

# assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

# client connection
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC, 0)

client.loop_forever()
