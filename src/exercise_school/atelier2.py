import random


def random_number():
    rand_number = None
    while rand_number != 6:
        rand_number = random.randint(1, 12)
        yield rand_number


generator = random_number()
while True:
    print(next(generator))


