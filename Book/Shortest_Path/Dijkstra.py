from operator import truediv
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n: node, m: 간선
start = int(input())

graph = [[] for i in range(n+1)]
visited = [ False for i in range(n+1)]
distance = [ INF for i in range(n+1)]
visited[start] = True
distance[start] = 0

# graph input
for i in range(1, m+1) :
    v, u, dist = map(int, input().split())
    graph[v].append((u, dist))

def unvisited_shortest_node(visited, distance) :
    temp = distance.copy()

    path = min(temp)
    v = temp.index(path)

    if not visited[v] :
        return v
    else :
        temp.pop(v)


def dijkstra() :
    for _ in range(n-1) :
        v = unvisited_shortest_node(visited, distance)

        for x in graph[v] :
            u, d = x[0], x[1]
            
            if distance[v] + d < distance[u] :
                distance[u] = distance[v] + d

dijkstra() # excecute

for d in distance[1:] :
    print(d)