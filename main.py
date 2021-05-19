import time
import MQTT
import random
import json
import datetime

host = "localhost"
port = 1883


def data_dth22(host, port, topic, frequency):
    mqtt = MQTT.MQTT(host, port).connect()

    while True:
        print("MQTT: publish on topic " + topic)
        data = {
            "payload": {
                "temperature": random.randint(0, 35),
                "humidity": random.randint(0, 100)
            },
            "metadata": {
                "macAddress": "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                                                           random.randint(0, 255),
                                                           random.randint(0, 255)),
                "device": "ESP8266",
                "location": "City, Street, nr / coordinates",
                "timestamp": datetime.datetime.now(),
                "maintainer": "Mr. X",
                "lastMaintain": datetime.datetime.now()
            }

        }

        mqtt.publish(topic, json.dumps(data, indent=4, sort_keys=True, default=str))
        time.sleep(frequency)


def main():
    data_dth22(host, port, "city/street", 1)


if __name__ == "__main__":
    main()
