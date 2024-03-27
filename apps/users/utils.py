import string
import random


def generate_token(n: int = 30):
    return "".join(
        (random.choice(string.ascii_letters + string.digits) for _ in range(n))
    )
