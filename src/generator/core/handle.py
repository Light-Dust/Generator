import logging
from random import randint

LOGGER = logging.Logger("generator")


def random_uuid() -> list[int]:
    a = randint(-2 ** 31, 2 ** 31 - 1)
    b = randint(-2 ** 31, 2 ** 31 - 1)
    c = randint(-2 ** 31, 2 ** 31 - 1)
    d = randint(-2 ** 31, 2 ** 31 - 1)
    return [a, b, c, d]
