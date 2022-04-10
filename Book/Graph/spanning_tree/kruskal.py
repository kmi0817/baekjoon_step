import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [ i for i in range(v+1) ]
q = []

# 간선 입력 받기
for _ in range(e) :
    x, y, d = map(int, input().split())
    heapq.heappush(q, (d, (x, y)))

def find_root(node) :
    if parent[node] != node :
        parent[node] = find_root(parent[node])
    return parent[node]

def kruskal() :
    cost = 0

    while q :
        c, pair = heapq.heappop(q)
        child = min(parent[pair[0]], parent[pair[1]])
        parent[child] = find_root(max(parent[pair[0]], parent[pair[1]]))
        if parent[pair[0]] != parent[pair[1]] :
            cost += c
            print(pair, cost)
            
            parent[pair[0]] = -1
            parent[pair[1]] = -1

    return cost

# Kruskal 실행
minimum_cost = kruskal()
print(minimum_cost)