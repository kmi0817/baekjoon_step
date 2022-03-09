global N
global M
N, M = map(int, input().split())

global step
step = 0
def dfs(graph, x, y) :
    if x == N and y == M :
        step += 1
        return

    if graph[x][y] == 1 and x <= N and y <= M :
        graph[x][y] = 0 # 방문 처리
        step += 1
        dfs(graph, x, y+1)
        dfs(graph, x+1, y)

# graph
graph = [[]]
for n in range(N) :
    graph.append(list(map(int, input())))


dfs(graph, 1, 1)
print(step)