from my_practice.finite_automaton_lexer import solution


def test_solution_1():
    data = [
        '  first second\n',
        'hello  my\n',
        'what   who   \n\n',
    ]

    expected = [
        'first',
        'hello',
        'what',
    ]

    assert solution(data) == expected


def test_solution_2():
    data = [
        '\n\n  what who   \n',
        'hellomy\n',
        ' hello who are you\n',
    ]

    expected = [
        'what',
        'hellomy',
        'hello',
    ]

    assert solution(data) == expected


def test_solution_3():
    data = [
        '\n\n  hi   \n',
        'hey how are you doing?\n',
        ' hello who are you',
    ]

    expected = [
        'hi',
        'hey',
        'hello',
    ]

    assert solution(data) == expected


def test_solution_4():
    data = [
        '\n\n  hi   \n',
        'hi how are you doing?\n',
        ' hello who are you',
    ]

    expected = [
        'hi',
        'hi',
        'hello',
    ]

    assert solution(data) == expected


def test_solution_5():
    data = [
        '\n\n  hi   \n',
        'hi how are you doing?\n',
        ' hello',
    ]

    expected = [
        'hi',
        'hi',
        'hello',
    ]

    assert solution(data) == expected
