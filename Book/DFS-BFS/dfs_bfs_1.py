N, M = map(int, input().split())

# graph
graph = []
for _ in range(N) :
    row = input()
    temp = []
    for r in row :
        temp.append(int(r))
    graph.append(temp)

def dfs(x, y) :
    if x <= -1 or x >= N or y <=-1 or y >= M :
        return False

    if graph[x][y] == 0 :
        graph[x][y] = 1 # 방문 처리

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else :
        return False

result = 0
for r in range(N) :
    for c in range(M) :
        if dfs(r, c) :
            result += 1
print(result)
