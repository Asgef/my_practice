from hexlet_code.helpers import build_prefix_tree
from itertools import chain


# Реализуйте функцию find_words(), которая найдет в
# префиксном дереве все слова, начинающиеся с указанного
# префикса и вернет их в отсортированном по алфавиту виде.

# find_words(words, 'appre')
# # ['apprehend', 'appreciate', 'apprentice'];


def find_words(tree, prefix):
    result = []

    def find_prefix_node(tree, text):
        node = tree
        if not text:
            return node
        for i, char in enumerate(text):
            if not node.children.get(char):
                return node
            node = node.children[char]
            return find_prefix_node(node, text[i + 1:])

    def find_suffixes(tree, prefix_char_list):
        node = tree

        prefix_char_list.append(node.key)

        if node.end:
            result.append(''.join(prefix_char_list))
            return

        for key in node.children.keys():
            find_suffixes(node.children[key], prefix_char_list.copy())

    suffixes_tree = find_prefix_node(tree, prefix)
    find_suffixes(suffixes_tree, list(prefix[:-1]))
    result.sort()

    return result


# Teacher's decision:

# def find_words(root, prefix):
#     currentNode = root
#     for char in prefix:
#         if char not in currentNode.children:
#             return []
#         currentNode = currentNode.children[char]
#
#     words = []
#
#     def traverse(node, word):
#         if node.end:
#             words.append(word + node.key)
#
#         for childKey in node.children.keys():
#             traverse(node.children[childKey], word + node.key)
#
#     traverse(currentNode, prefix[:-1])
#
#     return sorted(words)
