from operator import truediv
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n: node, m: 간선
start = int(input())

graph = [[] for i in range(n+1)]
visited = [ False for i in range(n+1)]
distance = [ INF for i in range(n+1)]

# graph input
for i in range(1, m+1) :
    v, u, dist = map(int, input().split())
    graph[v].append((u, dist))

def unvisited_shortest_node() :
    min_path = distance[0]
    index = 0

    for i in range(1, n+1) :
        if distance[i] < min_path and not visited[i] :
            min_path = distance[i]
            index = i
    
    return index

def dijkstra(start) :
    visited[start] = True
    distance[start] = 0

    for x in graph[start] :
        distance[x[0]] = x[1]

    for _ in range(n-1) :
        v = unvisited_shortest_node()
        # print(f"v: {v}")
        for x in graph[v] :
            u, d = x[0], x[1]
            
            if distance[v] + d < distance[u] :
                # print(f"distance[{u}] was {distance[u]}", end=" ")
                distance[u] = distance[v] + d
                # print(f"but now, it's {distance[u]}")
        visited[v] = True

dijkstra(start) # excecute

for d in distance[1:] :
    print(d)