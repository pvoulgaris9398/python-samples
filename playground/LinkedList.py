class Node:
    def __init__(self, data):
        self.data = data
        self.next_node: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Helper function to add items to the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = new_node

    def __iter__(self):
        """Returns the iterator object (the list instance itself)."""
        # When iteration begins, set a temporary pointer to the start of the list.
        self._current_node = self.head
        return self

    def __next__(self):
        """Returns the next data item in the sequence."""
        if self._current_node:
            # Get the current data
            data = self._current_node.data
            # Move the pointer to the next node
            self._current_node = self._current_node.next_node
            # Return the data
            return data
        else:
            # If the current pointer is None (end of list), stop iteration.
            raise StopIteration


# Create a linked list instance
my_list = LinkedList()

# Append some data
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Iterate over the linked list using a for loop
print("Iterating over the linked list:")
for item in my_list:
    print(item)
