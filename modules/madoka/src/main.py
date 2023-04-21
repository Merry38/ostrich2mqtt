import time
import os
from typing import Optional
from logging import Logger, getLogger

from madoka_client import MadokaClient
from mosquitto_client import MqttClient

def run(logger: Logger, eaton_url: str, mqtt_url: str):
    logger.info(f"Running Madoka for server {eaton_url} -> {mqtt_url}")

    # TODO
    # Initialize Madoka bt client 
    # Initialize MQTT client
    madoka = MadokaClient(eaton_url)
    mqtt = MqttClient(mqtt_url)
    
    while True:
        if not madoka.is_ready():
            logger.info(f"Unable to reach Eaton xStorage at url {madoka.get_url()}")
            continue

        if not mqtt.is_ready():
            logger.info(f"Unable to reach MQTT broker at url {mqtt.get_url()}")
            continue

        print("MMAAAAAA")

        time.sleep(1)


if __name__ == "__main__":
    log_level = os.getenv("LOG_LEVEL", "INFO")

    logger = getLogger()
    logger.setLevel(log_level)

    madoka_url: Optional[str] = os.getenv("MADOKA_URL", None)
    mqtt_url: Optional[str] = os.getenv("MQTT_URL", None)

    if madoka_url is None or mqtt_url is None:
        raise AttributeError(f"Invalid parameters provided {madoka_url} {mqtt_url}")

    run(logger, madoka_url, mqtt_url)