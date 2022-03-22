import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n: 노드 수, m: 간선 수
start = int(input()) # 시작노드

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
heap = [] # 우선순위 큐

for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# dijkstar
visited[start] = True
distance[start] = 0
for x in graph[start] :
    # x = (b, c) and b: node, c: path
    node, path = x[0], x[1]
    distance[node] = path
    heapq.heappush(heap, (path, node))

while heap :
    # print(heap)
    popped = heapq.heappop(heap)
    path, node = popped[0], popped[1]
    if not visited[node] :
        visited[node] = True

        for x in graph[node] :
            u, d = x[0], x[1]
            
            if distance[node] + d < distance[u] :
                distance[u] = distance[node] + d
                heapq.heappush(heap, (d, u))

for d in distance[1:] :
    print(d)