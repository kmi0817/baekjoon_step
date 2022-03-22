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

print(graph)