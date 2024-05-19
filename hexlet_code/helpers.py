from .tree_node import (
    BinaryTreeNode, RBTreeNode, BTreeNode, Trie
)


def sorted_array_to_BST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = BinaryTreeNode(nums[mid])
    root.left = sorted_array_to_BST(nums[:mid])
    root.right = sorted_array_to_BST(nums[mid + 1:])

    return root


def build_RBTree(data):
    root = RBTreeNode(data['value'])
    root.is_red = data['isRed']
    if 'left' in data and data['left']:
        root.left = build_RBTree(data['left'])
        root.left.parent = root
    if 'right' in data and data['right']:
        root.right = build_RBTree(data['right'])
        root.right.parent = root
    return root


def buildBTree(data):
    root = BTreeNode(data["keys"])
    root.leaf = data["leaf"]
    if not data["leaf"]:
        for child in data["children"]:
            root.children.append(buildBTree(child))
    return root


def build_prefix_tree(words):
    root = Trie(None)
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie(char)
            node = node.children[char]
        node.end = True
    return root
