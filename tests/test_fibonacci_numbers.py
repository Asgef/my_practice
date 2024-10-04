from my_practice.fibonacci_numbers import fib, gen_fib


def test_fibonacci():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55
    assert fib(15) == 610


def test_first_numbers():
    fib_gen = gen_fib()
    assert next(fib_gen) == 1
    assert next(fib_gen) == 1
    assert next(fib_gen) == 2
    assert next(fib_gen) == 3
    assert next(fib_gen) == 5

def test_infinite_sequence():
    fib_gen = gen_fib()
    numbers = [next(fib_gen) for _ in range(10)]
    assert numbers == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
