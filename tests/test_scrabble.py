from my_practice.scrabble import scrabble


def test_scrabble():
    assert scrabble('rkqodlw', 'world') is True
    assert scrabble('avj', 'java') is False
    assert scrabble('avjafff', 'java') is True
    assert scrabble('', 'hexlet') is False
    assert scrabble('scriptingjava', 'JavaScript') is True
