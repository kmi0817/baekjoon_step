import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

distance = [ [INF] * (n+1) for _ in range(n+1) ]
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            distance[i][j] = 0

for _ in range(m) :
    x, y = map(int, input().split())
    distance[x][y] = 1
    distance[y][x] = 1

x, k = map(int, input().split())

# floyd warshall
for i in range(1, n+1) :

    for k in range(1, n+1) :
        for l in range(1, n+1) :
            distance[k][l] = min(distance[k][l], distance[k][i] + distance[i][l])

result = distance[1][k] + distance[k][x]
if result > INF :
    print(-1)
else :
    print(result)