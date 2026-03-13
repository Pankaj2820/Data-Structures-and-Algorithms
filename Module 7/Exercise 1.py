def DFS(graph, u, visited=None):
    if visited is None:
        visited = {u: None}

    for v in graph._adj_map[u]:
        if v not in visited:
            visited[v] = u
            DFS(graph, v, visited)

    return visited