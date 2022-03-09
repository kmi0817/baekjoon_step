from collections import deque

N, M = map(int, input().split())

# graph
graph = []
for n in range(N) :
    graph.append(list(map(int, input())))
