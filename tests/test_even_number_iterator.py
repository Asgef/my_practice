from my_practice.even_number_iterator import EvenIterator


def test_even_iterator():
    iterator = EvenIterator()
    result = [num for num in iterator]

    assert result == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


