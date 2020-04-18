#!/usr/bin/python3

from smeterd.meter import SmartMeter
import paho.mqtt.client as mqtt
import json

MQTT_HOST = '192.168.1.2'
MQTT_PORT = 1883
MQTT_TOPIC = 'smart_meter'

meter = SmartMeter('/dev/ttyUSB0', baudrate=115200)
packet = meter.read_one_packet()

data = {
    "kwh_low": packet["kwh"]["low"]["consumed"],
    "kwh_high": packet["kwh"]["high"]["consumed"],
    "kwh_current": packet["kwh"]["current_consumed"],
    "gas": packet["gas"]["total"]
}

mqtt_client = mqtt.Client()
print("connecting to MQTT on {}:{}".format(MQTT_HOST, MQTT_PORT))
mqtt_client.connect(MQTT_HOST, MQTT_PORT)

mqtt_client.publish(
    MQTT_TOPIC,
    json.dumps(data)
)
