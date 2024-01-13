import string
import random

def create_random_code(length):
    chars = string.ascii_letters + string.digits + "_"
    return ''.join(random.choice(chars) for _ in range(length))