from collections import deque

global queue
queue = deque()
def bfs(graph, v, visited) :
    visited[v] = True
    print(v, end=" ")

    for node in graph[v] :
        if not visited[node] :
            queue.append(node)
            visited[node] = True

    try :
        bfs(graph, queue.popleft(), visited)
    except IndexError :
        pass

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

bfs(graph, 1, visited)