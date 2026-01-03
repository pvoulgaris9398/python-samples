class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


"""
Queue => FIFO model
"""


class ListBasedQueue:
    def __init__(self):
        self.list = []

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        if self.is_empty(self):
            return "Queue is empty!"
        else:
            return self.list.pop(0)

    def front(self):
        if self.is_empty(self):
            return "Queue is empty!"
        else:
            return self.list[0]

    def rear(self):
        if self.is_empty(self):
            return "Queue is empty!"
        else:
            return self.list[-1]

    def size(self):
        return len(self.list)

    def is_empty(self):
        return self.list == []


class StackBasedQueue:
    def __init__(self):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self, value):
        pass

    def front(self):
        pass

    def rear(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass


class NodeBasedQueue:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | Node = None

    def enqueue(self, value):
        pass

    def dequeue(self, value):
        pass

    def front(self):
        pass

    def rear(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        return self.Head is None and self.Tail is None
