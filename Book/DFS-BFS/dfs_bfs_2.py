from collections import deque

N, M = map(int, input().split())

# graph
graph = []
for n in range(N) :
    graph.append(list(map(int, input())))

# up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque([(x, y)])
    step = 1
    while queue :
        x, y = queue.popleft()

        for i in range(4) : # Check 4 directoins
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <=-1 or ny >= M :
                continue
            
            if graph[nx][ny] == 0 :
                continue
            
            if graph[nx][ny] == 1 :
                step += 1
                graph[nx][ny] = step
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0, 0))
