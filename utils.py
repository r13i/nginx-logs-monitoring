from random import randrange
from time import sleep

def mock_generator():
    """
    Generate mock ip address
    """

    sleep(1)
    return "{}.{}.{}.{}".format(
        randrange(256),
        randrange(256),
        randrange(256),
        randrange(256)
    )