import json
from datetime import datetime
from kafka import KafkaProducer
from service.const import (
    IssSatellite,
    Sentinel2A
)
from utils.json_parsers import (
    sentinel2a_message_from_json,
    iss_message_from_json
)
from utils.json_static import static_sentinel2a_message_from_json


class Producer:
    def __init__(
        self,
        data: json,
        is_iss=False,
        is_sentinel=False,
        is_fake=False,
    ):
        self.__data = data
        self.__is_iss = is_iss
        self.__is_sentinel = is_sentinel
        self.__is_fake = is_fake
        self.__checkpoint()

    def __checkpoint(self) -> None:
        """Get the useful coordinates on map"""

        """
        1. data: validating if there is no data
        2. is_fake: if True we'll get local data    
        """
        if not self.__data and not self.__is_fake:
            return

        try:
            if self.__is_iss:
                self.__producing(
                    IssSatellite.KAFKA_BROKER.value,
                    IssSatellite.KAFKA_TOPIC.value,
                    iss_message_from_json(self.__data)
                )

            if self.__is_sentinel:
                message = sentinel2a_message_from_json(self.__data) if not self.__is_fake \
                    else static_sentinel2a_message_from_json()

                self.__producing(
                    Sentinel2A.KAFKA_BROKER.value,
                    Sentinel2A.KAFKA_TOPIC.value,
                    message
                )
        except Exception as err:
            print(f"\nThere is an Exception: {err}")

    def __producing(
            self,
            server: str,
            topic: str,
            payload: bytes
    ) -> None:
        """
        Producing Kafka message
        :param server: the url kafka broker
        :param topic: the message topic
        :param payload: the message queue
        :return: None
        """
        producer = KafkaProducer(
            bootstrap_servers=server
        )
        message = payload
        producer.send(
            topic,
            message.encode('utf-8')
        )
        print(f'\n{datetime.now()} - kafka message sent from producer \n{message}')
