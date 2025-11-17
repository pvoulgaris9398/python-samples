from algorithms.node import Node


def tree_dfs_template(root: Node, target):
    if root is None:
        return None
    if root.value == target:
        return root
    left = tree_dfs_template(root.left, target)
    if left is not None:
        return left
    return tree_dfs_template(root.right, target)


def get_neighbors_template(root: Node):
    return []


def graph_dfs_template(root: Node, visited: set):
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        graph_dfs_template(neighbor, visited)


def backtracking_dfs_template(start_index, path, additional):
    ans = []

    def is_leaf(x):
        True

    def is_valid(x):
        False

    def get_edges(x):
        return []

    if is_leaf(start_index):
        ans.append(path[:])  # add a copy of the path to the result
        return
    for edge in get_edges(start_index):
        # prune if needed
        if not is_valid(edge):
            continue

        path.add(edge)
        # if additional states:
        #   update(...additional states)
        backtracking_dfs_template(start_index + len(edge, path, []))
        # revert(...additional states) if necessary, e.g. permutations
        path.pop()


def get_neighbors(grid, row, column):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for d in directions:
        new_row, new_column = row + d[0], column + d[1]
        if (
            0 <= new_row < len(grid)
            and 0 <= new_column < len(grid[0])
            and grid[new_row][new_column] == "1"
        ):
            neighbors.append((new_row, new_column))
    return neighbors


def dfs(grid, row, column, visited):
    visited.add((row, column))
    for neighbor in get_neighbors(grid, row, column):
        if neighbor in visited:
            continue
        dfs(grid, neighbor[0], neighbor[1], visited)


"""
WIP
Depth-First Search Example
"""


def main():
    print("Depth-First Search Example")


if __name__ == "__main__":
    main()
