INF = float("infinity")

graph = {
    "U": {"V": 6, "W": 7},
    "V": {"U": 6, "X": 10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10},
}

unvisited_min_distances = {vertex: INF for vertex in graph}
visited_vertices = {}
current_vertex = "U"
unvisited_min_distances[current_vertex] = 0

# While any vertices remain unvisited
while len(unvisited_min_distances) > 0:
    # Visit unvisited vertex with smallest known distance from the start vertex
    current_vertex, current_distance = sorted(
        unvisited_min_distances.items(), key=lambda x: x[1]
    )[0]  # Not efficient, use priority queue instead

    # For each unvisited neighbor of the current vertex
    for neighbor, neighbor_distance in graph[current_vertex].items():
        # If a neighbor has been processed (visited), skip it
        if neighbor in visited_vertices:
            continue

        # Calculate the new distance if this route is taken
        potential_new_distance = current_distance + neighbor_distance

        # If the calculated distance is less than the known distance...
        if potential_new_distance < unvisited_min_distances[neighbor]:
            # update it
            unvisited_min_distances[neighbor] = potential_new_distance

        # Mark current vertext as visited
        visited_vertices[current_vertex] = current_distance

        print(unvisited_min_distances)
        print(current_vertex)
        # Remove current vertext from unvisited nodes
        del unvisited_min_distances[current_vertex]

# print(visited_vertices.items())


def main():
    print(graph)


if __name__ == "__main__":
    main()
