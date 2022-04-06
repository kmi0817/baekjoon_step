import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [ [] for _ in range(n+1) ]

for _ in range(m) :
    v, u = map(int, input().split())
    graph[v].append(u)

x, k = map(int, input().split())

# dijkstra
def dijkstra(start, target) :
    distance = [INF] * (n+1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for i in graph[now] :
            distance[i] = min(distance[i], distance[now] + 1)
            heapq.heappush(q, (distance[i], i))

    return distance[target]

a = dijkstra(1, x)
b = dijkstra(x, k)

print(a+b)