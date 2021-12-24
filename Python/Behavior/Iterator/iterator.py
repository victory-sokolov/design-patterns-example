from typing import Iterator

def count_to(count):

    fruits = ["apple", "banana", "peach", "orange"]

    # create tuple
    iterator = zip(range(count), fruits)

    for position, fruit in iterator:
        yield fruit

for fruit in count_to(3):
    print(fruit)
