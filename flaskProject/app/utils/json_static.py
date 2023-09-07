from datetime import datetime
from flask import json
import uuid


data = {}
data_items = []


def static_sentinel2a_message_from_json() -> bytes:
    """
    Arranging sentinel payload
    """
    static_file = open('./data/sentinel.json')
    json_array = json.load(static_file)
    coordinates = json_array['features'][0]['geometry']['coordinates']

    data = generating(coordinates)
    return json.dumps(data)


def generating(
        coordinates
) -> dict:

    count = len(data_items)
    index = count + 1

    data["key"] = uuid.uuid4()
    data["id"] = 40697
    data["latitude"] = coordinates[index][1]
    data["longitude"] = coordinates[index][0]
    data["timestamp"] = str(datetime.utcnow())

    data_items.append(data)
    return data
