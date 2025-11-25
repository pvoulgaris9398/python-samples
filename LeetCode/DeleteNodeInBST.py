class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode.com/problems/delete-node-in-a-bst
"""


class Solution:
    def deleteNode(self, root, key):
        print()


def build(array, start: int, end: int, root):
    if start > end:
        return None

    mid = int((start + end) / 2)

    if root is None:
        root = TreeNode(array[mid])

    root.left = build(array, start, mid - 1, root.left)
    root.right = build(array, mid + 1, end, root.right)

    return root


def find_node(root, node):
    if root.left is None and root.right is None:
        return None
    if root.left is not None and root.left == node:
        return root.left
    if root.right is not None == node:
        return root.right

    if root.left is not None and root.left.val > node.val:
        return find_node(root.left, node)
    elif root.right is not None and root.right.val > node.val:
        return find_node(root.right, node)


def delete_node(root, node):
    found = find_node(root, node)
    print(found)


def test0():
    array = [5, 3, 6, 2, 4, None, 7]
    root = build(array, 0, len(array) - 1, None)
    delete_node(root, TreeNode(3))
    print(root)


def main():
    test0()


if __name__ == "__main__":
    print()
    main()
