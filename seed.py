import random

t = random.randint(0, 2**32 - 1)

def seed_generator():
    seed = t
    return seed