import string
import random
import re

def create_random_code(length):
    chars = string.ascii_letters + string.digits + "_"
    return ''.join(random.choice(chars) for _ in range(length))
    
def validate_code(shortcode):
    if len(shortcode) != 6 or not re.fullmatch(r'[A-Za-z0-9_]*$', shortcode):
        return False
    return True