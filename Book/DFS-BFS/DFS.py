def dfs(graph, v, visited) :
    visited[v] = True # 방문 처리
    print(v, end=" ")
    for node in graph[v] :
        if not visited[node] :
            visited[node] = True
            dfs(graph, node, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False for _ in range(9)]

dfs(graph, 1, visited)