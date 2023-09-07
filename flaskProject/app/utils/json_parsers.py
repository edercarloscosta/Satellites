from flask import json
import uuid


data = {}


def iss_message_from_json(
        coordinates
) -> bytes:
    """
    Arranging iss payload
    """
    data["key"] = uuid.uuid4()
    data["id"] = coordinates["id"]
    data["latitude"] = coordinates["latitude"]
    data["longitude"] = coordinates["longitude"]
    data["timestamp"] = coordinates["timestamp"]

    return json.dumps(data)


def sentinel2a_message_from_json(
        coordinates
) -> bytes:
    """
    Arranging sentinel payload
    """
    positions = coordinates['positions']
    indice = positions[0]
    id = coordinates['info']

    data["key"] = uuid.uuid4()
    data["id"] = id["satid"]
    data["latitude"] = indice["satlatitude"]
    data["longitude"] = indice["satlongitude"]
    data["timestamp"] = indice["timestamp"]

    return json.dumps(data)
