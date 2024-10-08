from my_practice.gpt_caching_decorator import cache_decorator


def test_cache_with_same_args():
    @cache_decorator
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
    assert add(1, 2) == 3  # Должно взять результат из кэша
    assert add(2, 3) == 5


def test_cache_with_different_types():
    @cache_decorator
    def multiply(a, b):
        return a * b

    assert multiply(2, 3) == 6
    assert multiply(2.0, 3) == 6.0  # Разные типы аргументов - не из кэша
    assert multiply(2.0, 3) == 6.0  # В этот раз из кэша


def test_cache_with_named_args():
    @cache_decorator
    def subtract(a, b):
        return a - b

    assert subtract(a=5, b=3) == 2
    assert subtract(a=5, b=3) == 2  # Должно взять результат из кэша
    assert subtract(b=3, a=5) == 2  # Аргументы по имени, другой порядок


def test_cache_with_complex_arguments():
    @cache_decorator
    def concat_strings(*args):
        return ''.join(args)

    assert concat_strings('a', 'b') == 'ab'
    assert concat_strings('a', 'b') == 'ab'  # Из кэша
    assert concat_strings('a', 'c') == 'ac'


def test_cache_edge_cases():
    @cache_decorator
    def division(a, b):
        return a / b

    assert division(10, 2) == 5
    assert division(10, 2) == 5  # Из кэша
    assert division(0, 1) == 0
