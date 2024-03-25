from my_practice.string_and_stack import stack_lexem


def test_stack_lexem():
    assert stack_lexem('ab#c', 'ad#c') is True
    assert stack_lexem('ab##', 'c#d#') is True
    assert stack_lexem('a#c', 'b') is False
