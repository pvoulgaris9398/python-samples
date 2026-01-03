"""
Stack implementation, with some research/analysis
on how to implement iterators, etc.
Current WIP
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class Stack:
    def __init__(self):
        self.head: Node | None = None

    def __iter__(self):
        current = self.head
        while current is not None:
            print(f"current: {current.data}")
            yield f"{current.data},"
            current = current.next

    # def __iter__(self):
    #     """Returns the iterator object (the list instance itself)."""
    #     # When iteration begins, set a temporary pointer to the start of the list.
    #     self._current_node = self.head
    #     return self

    def __next__(self):
        """Returns the next data item in the sequence."""
        if self._current_node:
            # Get the current data
            data = self._current_node.data
            # Move the pointer to the next node
            self._current_node = self._current_node.next
            # Return the data
            return data
        else:
            # If the current pointer is None (end of list), stop iteration.
            raise StopIteration

    def __str__(self):
        for i in self:
            print(f"test: {i}")
        return "foo"
        # "".join(i for i in self)

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            return None
        else:
            node = self.head
            self.head = node.next  # Could be None, that's OK
            node.next = None
            return node

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


def is_palindrome(s):
    s = s.lower()
    s = "".join(c for c in s if c.isalnum())

    stack = Stack()
    for c in s:
        stack.push(s)

    print(stack)
    for c in s:
        if c != stack.pop().data:
            return False

    return True


def test0():
    s = "a man, a plan, a canal!!! - Panama"
    result = is_palindrome(s)
    print(f"'{s}' ... {"is" if result else "is not"} a palindrome!")


def test1():
    s = "anna"
    result = is_palindrome(s)
    print(f"'{s}' ... {"is" if result else "is not"} a palindrome!")


def main():
    test1()


if __name__ == "__main__":
    main()
