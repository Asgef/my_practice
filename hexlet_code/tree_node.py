class BinaryTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class RBTreeNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.is_red = False
        self.parent = parent
        self.value = value


class BTreeNode:
    def __init__(self, keys):
        self.leaf = False
        self.keys = keys
        self.children = []


class Trie:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.end = False
