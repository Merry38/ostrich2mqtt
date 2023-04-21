import time
import os
from typing import Optional
from logging import Logger, getLogger

from .eaton_client import EatonClient
from .mosquitto_client import MqttClient

def run(logger: Logger, eaton_url: str, mqtt_url: str):
    logger.info(f"Running xStorage for server {eaton_url} -> {mqtt_url}")

    # TODO
    # Initialize Eaton client 
    # Initialize MQTT client
    eaton = EatonClient(eaton_url)
    mqtt = MqttClient(mqtt_url)
    
    while True:
        if not eaton.is_ready():
            logger.info(f"Unable to reach Eaton xStorage at url {eaton.get_url()}")
            continue

        if not mqtt.is_ready():
            logger.info(f"Unable to reach MQTT broker at url {mqtt.get_url()}")
            continue

        print("EEAAAAAA")

        time.sleep(1)


if __name__ == "__main__":
    log_level = os.getenv("LOG_LEVEL", "INFO")

    logger = getLogger()
    logger.setLevel(log_level)

    eaton_url: Optional[str] = os.getenv("EATON_URL", None)
    mqtt_url: Optional[str] = os.getenv("MQTT_URL", None)

    if eaton_url is None or mqtt_url is None:
        raise AttributeError(f"Invalid parameters provided {eaton_url} {mqtt_url}")

    run(logger, eaton_url, mqtt_url)