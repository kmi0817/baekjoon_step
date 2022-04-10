import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())

graph = [ [] for _ in range(v+1) ]
depth = [0] * (v+1)

# 입력
for _ in range(e) :
    first, second = map(int, input().split())
    graph[first].append(second)
    depth[second] += 1

print(depth)

def topology_sort(start) :
    q = deque()
    q.append(start)

    while q :
        x = q.popleft()
        print(x, end=" ")
        for y in graph[x] :
            if depth[y] > 0 :
                depth[y] -= 1

                if depth[y] == 0 :
                    q.append(y)

topology_sort(1)