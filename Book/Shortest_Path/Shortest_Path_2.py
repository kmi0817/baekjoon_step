import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

distance = [ [INF] * (n+1) for _ in range(n+1) ]

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

for row in distance :
    for col in row :
        print(col, end=" ")
    print()

if distance[1][k] < INF and distance[k][x] :
    print(distance[1][k] + distance[k][l])
else :
    print(-1)