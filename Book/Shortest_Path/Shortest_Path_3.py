import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

distance = [INF] * (n+1)
graph = [ [] for _ in range(n+1) ]

# input graph
for _ in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# Dijkstra Algorithm
def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        d, v = heapq.heappop(q)

        if distance[v] < d :
            continue

        for i in graph[v] :
            distance[i[0]] = min(distance[v] + i[1], distance[i[0]])
            heapq.heappush(q, (distance[i[0]], i[0]))

dijkstra(c)

# avaiable city count and total time
max_value = -1
city_cnt = 0
for i, d in enumerate(distance[1:]) :
    if d != INF :
        if i != c :
            city_cnt += 1
        if max_value < d :
            max_value = d

# print the result
print(city_cnt, max_value)