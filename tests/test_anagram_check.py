from my_practice.anagram_check import are_anagrams


def test_anagram():
    assert are_anagrams('Aba', 'aab') is True
    assert are_anagrams('Hello', 'Olleh') is True
    assert are_anagrams('abc', 'def') is False
    assert are_anagrams('123', '321') is True
    assert are_anagrams('', '') is True
    assert are_anagrams('listen', 'silent') is True
    assert are_anagrams('evil', 'vile') is True
    assert are_anagrams('Debit Card', 'Bad Credit') is True
    assert are_anagrams('Schoolmaster', 'The classroom') is False
