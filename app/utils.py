import uuid
import random


def factory_uuid4() -> str:
    return str(uuid.uuid4())


def factory_order_key() -> str:
    """
    Generate order_key like -> "NSO9812"
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    return ''.join(random.choices(alphabet, k=3)) + str(random.randint(1000, 9999))

