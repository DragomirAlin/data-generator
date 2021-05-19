import paho.mqtt.client as mqtt
import logging


class Publish(object):
    def __init__(self, host, port):
        self.connect = False
        self.host = host
        self.port = port
        self.client = None
        self.log = logging.getLogger(__name__)

    def on_message(self, client, userdata, msg):
        self.log.debug("MQTT: Publish message")

    def mqtt(self):
        try:
            self.client = mqtt.Client()
            status_connection = self.client.connect(self.host, self.port, keepalive=60)
            if status_connection == 0:
                self.log.info("Successfully connected to Broker!")
                self.connect = True
                return self
        except ConnectionRefusedError:
            self.log.error("Connection failed")
        except:
            self.log.error("Unknown error while connecting to Broker.")

    def start(self):
        self.client.loop_forever()
