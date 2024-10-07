# Реализуйте функцию find_words(), которая найдет в
# префиксном дереве все слова, начинающиеся с указанного
# префикса и вернет их в отсортированном по алфавиту виде.

# find_words(words, 'appre')
# # ['apprehend', 'appreciate', 'apprentice'];


from hexlet_code.tree_node import Trie


# def find_words(tree, prefix):  # noqa C901
    # result = []
    #
    # def find_prefix_node(tree, text):
    #     node = tree
    #     if not text:
    #         return node
    #     for i, char in enumerate(text):
    #         if not node.children.get(char):
    #             return node
    #         node = node.children[char]
    #         return find_prefix_node(node, text[i + 1:])
    #
    # def find_suffixes(tree, prefix_char_list):
    #     node = tree
    #
    #     prefix_char_list.append(node.key)
    #
    #     if node.end:
    #         result.append(''.join(prefix_char_list))
    #         return
    #
    #     for key in node.children.keys():
    #         find_suffixes(node.children[key], prefix_char_list.copy())
    #
    # suffixes_tree = find_prefix_node(tree, prefix)
    # find_suffixes(suffixes_tree, list(prefix[:-1]))
    # result.sort()
    #
    # return result


# Teacher's decision:


def find_words(tree: Trie, prefix: str) -> list[str]:
    prefix_node = tree
    for char in prefix:
        if char not in prefix_node.children:
            return []
        prefix_node = prefix_node.children[char]
    words = []

    def traverse(node: Trie, word: str) -> None:
        if node.end:
            words.append(word + node.key)

        for child in node.children.values():
            traverse(child, word + node.key)

    traverse(prefix_node, prefix[:-1])
    return sorted(words)




































