# Problem: "Associative Array"
# Implement and export a set of functions to work with an associative array
# (hash table) using crc32. To simplify, our implementation does not support
# collision resolution.
#
# set_(hash_table, key, value) — sets a value in the hash table by key.
# Works for both creating and updating. The function returns True if the
# value was successfully set. In case of a collision, the function does
# not change the hash table and returns False.
#
# get_(hash_table, key, default = None) — returns the value of the specified
# key. The default parameter is the value that the function returns if the
# key is not in the dictionary (default is None). In case of a collision,
# the function also returns the default value.

# Задача: "Ассоциативный массив"
# Реализуйте и экспортируйте набор функций для работы с ассоциативным
# массивом (хеш-таблицей) используя crc32. Чтобы было проще, наша
# реализация не поддерживает разрешение коллизий.
#
# set_(hash_table, key, value) — устанавливает в хеш-таблицу значение
# по ключу. Работает и для создания, и для изменения. Функция возвращает
# True, если удалось установить значение. При возникновении коллизии
# функция никак не меняет хеш-таблицу и возвращает False.
#
# get_(hash_table, key, default = None) — возвращает значение указанного
# ключа. Параметр default — значение, которое функция возвращает, если
# в словаре нет ключа (по умолчанию равно None). При возникновении
# коллизии функция также возвращает значение по умолчанию.

# Example:
# hash_table = {}
# set_(hash_table, 'key1', 'value1')  # True
# get_(hash_table, 'key1')  # 'value1'
# get_(hash_table, 'key2', 'default')  # 'default'
# set_(hash_table, 'key1', 'value2')  # True
# get_(hash_table, 'key1')  # 'value2'
# set_(hash_table, 'key2', 'value2')  # False (collision)
# get_(hash_table, 'key2', 'default')  # 'default'


from zlib import crc32
from typing import Optional
from hexlet_code.hash_table import make


def set_(map: make, key: str, value: str) -> bool:
    idx = get_index(key)

    if map[idx] and has_collisions(map, key):
        return False
    map[idx] = key, value
    return True


def get_(map: make, key: str, default: Optional[str] = None) -> Optional[str]:
    idx = get_index(key)

    if not map[idx] or has_collisions(map, key):
        return default
    return map[idx][1]


def get_index(key: str) -> int:
    b_key = key.encode('utf-8')
    return crc32(b_key) % 1000


def has_collisions(map, key: str) -> bool:
    idx = get_index(key)
    current_key, _ = map[idx]
    return current_key != key

# Хэш таблицы
