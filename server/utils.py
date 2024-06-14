import string
import random


def create_random_string(amount: int):
    return ''.join(random.choice(string.ascii_letters) for character in range(amount))
