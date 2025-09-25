import queue
from typing import Optional


class Node:
    def __init__(
        self, value, left: Optional["Node"] = None, right: Optional["Node"] = None
    ):
        self.value = value
        self.left = left
        self.right = right


def print_queue(d):
    q = queue.Queue()

    root = d
    current_level = 1

    q.put((root, current_level))

    while q.qsize() > 0:
        (current, level) = q.get()

        if current_level < level:
            current_level += 1

        print(current.value)

        if current.left is not None:
            q.put((current.left, level + 1))

        if current.right is not None:
            q.put((current.right, level + 1))


def invert_tree(node: Node) -> Node:
    if node is None:
        return None

    (node.left, node.right) = (invert_tree(node.right), invert_tree(node.left))

    return node


root = Node(4)
root.left = Node(2, Node(1), Node(3))
root.right = Node(7, Node(6), Node(9))

print_queue(root)

swapped = invert_tree(root)

print_queue(swapped)

"""
q = queue.Queue()

root = d
current_level = 1

q.put((root, current_level))

while q.qsize() > 0:
    (current, level) = q.get()

    if current_level < level:
        current_level += 1

    print(current.value)

    if current.left is not None:
        q.put((current.left, level + 1))

    if current.right is not None:
        q.put((current.right, level + 1))
"""
