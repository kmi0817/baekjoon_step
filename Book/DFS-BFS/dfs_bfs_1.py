N, M = map(int, input().split())

# graph
graph = []
for _ in range(N) :
    row = input()
    temp = []
    for r in row :
        temp.append(int(r))
    graph.append(temp)

def dfs(graph, v, visited, M) :
    visited[v] = True

    for u in range(M) :
        if graph[v][u] == 0 and not visited[v*M + u] :
            visited[v*M + u] = True

visited = [False for _ in range(N * M)]
