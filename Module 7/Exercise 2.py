def BFS(graph, start):
    """
    Perform Breadth-First Search starting at Vertex start.
    Returns a dictionary where:
        key = vertex
        value = vertex from which it was discovered
    """
    visited = {start: None}   # start has no parent
    queue = [start]           # use list as queue

    while queue:
        current = queue.pop(0)   # remove from front

        for neighbor in graph._adj_map[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return visited