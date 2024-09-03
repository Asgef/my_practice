from my_practice.finite_automaton_lexer import lexer  # , solution


# def test_solution_1():
#     data = [
#         '  first second\n',
#         'hello  my\n',
#         'what   who   \n\n',
#     ]
#
#     expected = [
#         'first',
#         'hello',
#         'what',
#     ]
#
#     assert lexer(data) == expected
#
#
# def test_solution_2():
#     data = [
#         '\n\n  what who   \n',
#         'hellomy\n',
#         ' hello who are you\n',
#     ]
#
#     expected = [
#         'what',
#         'hellomy',
#         'hello',
#     ]
#
#     assert lexer(data) == expected


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

    assert lexer(data) == expected


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

    assert lexer(data) == expected


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

    assert lexer(data) == expected


def test_lexer():
    assert lexer('singleline') == ['singleline']
    assert lexer('   ') == []
    assert lexer('\n\n\n') == []
    assert lexer(
        '  what who   \nhellomy\n hello who are you\n'
    ) == ['what', 'hellomy', 'hello']
    assert lexer(
        '    \n    \n hello\n world\n '
    ) == ['hello', 'world']
    assert lexer(
        'one two three\nfour\n five six seven'
    ) == ['one', 'four', 'five']
    assert lexer(
        '  multiple   spaces   here \n and \n here '
    ) == ['multiple', 'and', 'here']
    assert lexer(
        '\n\n\n   \nfirst\n  \n  second\nthird\n'
    ) == ['first', 'second', 'third']
    assert lexer(
        'firstword\n   \n\n lastword'
    ) == ['firstword', 'lastword']
    assert lexer(
        '    start\n middle\n end '
    ) == ['start', 'middle', 'end']
