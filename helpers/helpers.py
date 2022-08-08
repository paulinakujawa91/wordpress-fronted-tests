import random


def get_random_string():
    ints = range(33, 127)
    random_string = ''

    for i in range(10):
        random_string += chr(random.choice(ints))
    return random_string
