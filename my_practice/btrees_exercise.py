from hexlet_code.helpers import buildBTree


# Вам предстоит поработать с B-деревом.
# Напишите функцию, которая найдет в B-дереве все значения,
# находящиеся в заданном
#
# find_values_in_range(items, 30, 50)
# ## [31, 41, 47]


def find_values_in_range(items, min, max):
    result = []

    def walk(node, min, max):
        for key in node.keys:
            if min <= key <= max:
                result.append(key)
            elif key > max:
                break
        if not node.leaf:
            children = list(filter(
                None, map(lambda child: walk(child, min, max), node.children)
            ))
            result.extend(children)
            return
    walk(items, min, max)
    result.sort()

    return result


def solution(items, min, max):
    btree = buildBTree(items)
    return find_values_in_range(btree, min, max)
