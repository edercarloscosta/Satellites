"""
Author Note: KafkaProducer
Once decoupled from docker-compose you should stop
listening from kafka:9092 instead add localhost:9092
because kafka:x is container network
"""
from choicesenum import ChoicesEnum

PERSONAL_KEY = 'personal_key_here'


class IssSatellite(ChoicesEnum):
    ISS_URI = "https://api.wheretheiss.at/v1/satellites/25544"
    KAFKA_BROKER = 'kafka:9092'
    KAFKA_TOPIC = 'iss_satellite'
    KAFKA_GROUP_ID = 'iss_satellite_group'


class Sentinel2A(ChoicesEnum):
    SENTINEL2A_URI = f'https://api.n2yo.com/rest/v1/satellite/positions/40697/41.702/-76.014/0/2/&apiKey={PERSONAL_KEY}'
    KAFKA_BROKER = 'kafka:9092'
    KAFKA_TOPIC = 'sentinel2a_satellite'
    KAFKA_GROUP_ID = 'sentinel2a_satellite_group'
