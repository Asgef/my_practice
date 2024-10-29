from collections.abc import Generator, Iterable
from typing import Any


def numbers(n: int) -> Generator[str, None, None]:
    for i in range(n):
        yield f'numbers {i}'


def wrapper(g: Generator) -> Generator[Any, None, None]:
    yield 'wrapper: first value'
    for element in g:
        yield element
    yield 'wrapper: last value'

gen: Generator[Any, None, None] = wrapper(numbers(3))

# 'wrapper: first value',
#  'numbers 0',
#  'numbers 1',
#  'numbers 2',
#  'wrapper: last value'

############################################################################


def wrapper(g: Generator) -> Generator[Any, None, None]:
    yield 'wrapper: first value'
    yield from g
    yield 'wrapper: last value'

gen: Generator[Any, None, None] = wrapper(numbers(3))

# 'wrapper: first value',
#  'numbers 0',
#  'numbers 1',
#  'numbers 2',
#  'wrapper: last value'

############################################################################


type Enumerator = Generator[tuple[int, Any], None, None]


def enumerations(iterable: Iterable) -> Enumerator:
    yield from enumerate(iterable, start=1)

enumerator: Enumerator = enumerations('ABCDEF')


# [
#     (1, 'A'),
#     (2, 'B'),
#     (3, 'C'),
#     (4, 'D'),
#     (5, 'E'),
#     (6, 'F')
# ]
