# Реализуйте функцию find_words(), которая найдет в
# префиксном дереве все слова, начинающиеся с указанного
# префикса и вернет их в отсортированном по алфавиту виде.

# find_words(words, 'appre')
# # ['apprehend', 'appreciate', 'apprentice'];


from hexlet_code.tree_node import Trie


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
