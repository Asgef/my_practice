from my_practice.associative_array import set_, get_
from hexlet_code.hash_table import make


def test_hash_table():
    hash_table = make()
    assert set_(hash_table, 'key1', 'value1') is True
    assert get_(hash_table, 'key1') == 'value1'
    assert get_(hash_table, 'key2', 'default') == 'default'
    assert set_(hash_table, 'key1', 'value2') is True
    assert get_(hash_table, 'key1') == 'value2'
    assert set_(hash_table, 'key25', 'value25') is True
    assert set_(hash_table, 'key50', 'value50') is False
    assert get_(hash_table, 'key50', 'default') == 'default'
