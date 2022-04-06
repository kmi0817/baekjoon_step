INF = int(1e9)

n = int(input())
m = int(input())

# create 2-d list
distance = [ [ [] for _ in range(n+1) ] for _ in range(n+1) ]

# initialize list
for i in range(n+1) :
    for j in range(n+1) :
        if i == j :
            distance[i][j] = 0
        else :
            distance[i][j] = INF

# input
for _ in range(m) :
    x, y, d = map(int, input().split())
    distance[x][y] = d

# floyd warshall
for i in range(1, n+1) :
    for k in range(1, n+1) :
        for l in range(1, n+1) :
            distance[k][l] = min(distance[k][l], distance[k][i] + distance[i][l])

# print
for i in range(1, n+1) :
    for j in range(1, n+1) :
        print(distance[i][j], end=" ")
    print()