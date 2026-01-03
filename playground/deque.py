from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


"""

Can operate as LIFO or FIFO
Can add/remove at both ends of the data structure
Double-ended queue

"""


class Dequeu:
    def __init__(self):
        pass

    def append_left(self):
        pass

    def pop_left(self):
        pass

    def append_right(self):
        pass

    def pop_right(self):
        pass

    def reverse(self):
        pass

    def rotate(self):
        pass

    def extend(self):
        pass


my_deque = deque([1, 2, 3, 4, 5])

print(my_deque)

my_deque.rotate(2)

print(my_deque)

my_deque.reverse()

print(my_deque)

my_deque.extend([6, 7, 8])

print(my_deque)

my_deque.extendleft([-3, -4, 5])

print(my_deque)
