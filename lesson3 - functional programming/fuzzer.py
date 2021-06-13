import random
import itertools

"""Generate an infinite stream of successively larger random lists."""


def generate_cases():
    length = 0
    while True:
        lst = [random.randrange(0, 9, 1) for i in range(length)]
        yield lst
        length += 1


def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))


# generator iterator
def generate_cases_alternative():
    # yield from (random_list(size) for size in itertools.count())
    return (random_list(size) for size in itertools.count())


def generate_cases_another_alternative():
    return map(random_list, itertools.count())

if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)