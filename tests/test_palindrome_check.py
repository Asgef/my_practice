from my_practice.palindrome_check import is_palindrome


def test_palindrome():
    assert is_palindrome('qwertytrewq') is True
    assert is_palindrome('qweqwtwe') is False
    assert is_palindrome('anna') is True
    assert is_palindrome('annet') is False
    assert is_palindrome('radar') is True
    assert is_palindrome('level') is True
    assert is_palindrome('deified') is True
