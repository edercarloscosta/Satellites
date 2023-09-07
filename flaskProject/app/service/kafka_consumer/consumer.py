from kafka import KafkaConsumer
from datetime import datetime
from service.const import (
    IssSatellite,
    Sentinel2A
)


class Consumer:
    def __init__(
            self,
            is_iss=False,
            is_sentinel=False
    ):
        self.__is_iss = is_iss
        self.__is_sentinel = is_sentinel

    def checkpoint(self) -> KafkaConsumer:
        """Get the useful coordinates on map"""
        try:
            if self.__is_iss:
                return self.__consuming(
                    IssSatellite.KAFKA_TOPIC.KAFKA_BROKER.value,
                    IssSatellite.KAFKA_TOPIC.value,
                    IssSatellite.KAFKA_GROUP_ID.value
                )

            if self.__is_sentinel:
                return self.__consuming(
                    Sentinel2A.KAFKA_TOPIC.KAFKA_BROKER.value,
                    Sentinel2A.KAFKA_TOPIC.value,
                    Sentinel2A.KAFKA_GROUP_ID.value
                )
        except Exception as err:
            print(f"\nThere is an Exception: {err}")

    def __consuming(
            self,
            server: str,
            topic: str,
            group_id: str
    ) -> KafkaConsumer:
        """
        Consuming kafka message
        :param server: the url kafka broker
        :param topic: the message topic
        :param group_id: the group of readers
        :return: KafkaConsumer (the queue message)
        """
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=server,
            group_id=group_id
        )

        print(f'\n{datetime.now()} - kafka message read on consumer')
        return consumer
