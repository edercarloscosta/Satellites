from service.kafka_producer.producer import Producer
from service.kafka_consumer.consumer import Consumer
import threading
import requests
import json


class Worker:
    def __init__(
            self,
            uri: str,
            is_iss=False,
            is_sentinel=False,
    ):
        self.__uri = uri
        self.__is_iss = is_iss
        self.__is_sentinel = is_sentinel
        self.__producer()

    def __call_uri(self) -> json:
        """ Call the endpoint url provider """
        response = requests.get(self.__uri)
        return response.json()

    def __producer(self) -> None:
        """ Send data to producer """
        if not self.__uri:
            Producer(
                None,
                self.__is_iss,
                self.__is_sentinel,
                True
            )
        else:
            response = self.__call_uri()
            Producer(
                response,
                self.__is_iss,
                self.__is_sentinel
            )

        threading.Timer(15.0, self.__producer).start()

    def consumer(self):
        """ Consuming the kafka messages queue"""
        obj = Consumer(
            self.__is_iss,
            self.__is_sentinel
        )

        reading = obj.checkpoint()
        for c in reading:
            yield f'data:{c.value.decode()}\n\n'
