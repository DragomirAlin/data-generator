import time
import MQTT

host = "localhost"
port = 1883


def data_DTH22(host, port, topic, frequency):
    mqtt = MQTT.MQTT(host, port).connect()

    while True:
        print("MQTT: publish on topic " + topic)
        mqtt.publish(topic, "temperature")
        time.sleep(frequency)


def main():
    data_DTH22(host, port, "city/street", 1)


if __name__ == "__main__":
    main()
