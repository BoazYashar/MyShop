import random
import string

def generate_random_email(prefix):
    domain = "@example.com"
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{suffix}{domain}"