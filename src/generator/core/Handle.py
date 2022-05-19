import logging
from random import random

LOGGER = logging.Logger("generator")


def randomUUID() -> list[int]:
    a = int(random() * 100000000000000000) % (2 ** 32)
    b = int(random() * 100000000000000000) % (2 ** 32)
    c = int(random() * 100000000000000000) % (2 ** 32)
    d = int(random() * 100000000000000000) % (2 ** 32)
    return [a, b, c, d]
