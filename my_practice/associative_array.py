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


from hexlet_code.hash_table import make
from zlib import crc32


def set_(map, key, value):
    index = get_index(key)

    if map[index] and has_collision(map, key):
        return False
    map[index] = key, value
    return True


def get_(map, key, default=None):
    index = get_index(key)

    if not map[index] or has_collision(map, key):
        return default

    return map[index][1]


def get_index(key):
    b_key = to_b_str(key)
    return crc32(b_key) % 100


def has_collision(map, key):
    index = get_index(key)
    current_key, _ = map[index]
    return current_key != key


def to_b_str(string):
    return string.encode('utf-8')
