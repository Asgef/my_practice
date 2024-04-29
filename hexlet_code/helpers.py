from .tree_node import BinaryTreeNode
from .tree_node import RBTreeNode


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
