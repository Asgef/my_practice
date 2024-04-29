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
