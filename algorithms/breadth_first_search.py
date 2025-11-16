# from collections import queue


"""
def bfs_by_queue(root):
    queue = deque([root]):          # at least one element required
    while len(queue) > 0:           # as long as there is an element in the queue
        node = queue.pop_left()     # dequeue
        for child in node.children: # enqueue any children
            if (OK(child)):         # early return if problem condition is met
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND
"""


def main():
    # uses FIFO queue
    print("Breadth first search Example")


if __name__ == "__main__":
    main()
