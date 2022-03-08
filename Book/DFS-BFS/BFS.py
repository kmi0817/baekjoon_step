from collections import deque

# normal function
def bfs(graph, v, visited) :
    qu = deque([v])
    visited[v] = True

    while qu :
        node = qu.popleft()
        print(node, end=" ")
        for n in graph[node] :
            if not visited[n] :
                qu.append(n)
                visited[n] = True


# recursive function
global queue
queue = deque()
def bfs_recursive(graph, v, visited_) :
    visited[v] = True
    print(v, end=" ")

    for node in graph[v] :
        if not visited[node] :
            queue.append(node)
            visited[node] = True

    try :
        bfs_recursive(graph, queue.popleft(), visited)
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

# Both codes must not be executed together
# Just run it one by one!
bfs(graph, 1, visited)
bfs_recursive(graph, 1, visited)