import sys
input = sys.stdin.readline

def find_root(node) :
    if parent[node] != node :
        parent[node] = find_root(parent[node])
    return parent[node]
def union(a, b) :
    child = max(parent[a], parent[b])
    parent[child] = find_root(min(parent[a], parent[b]))

v, e = map(int, input().split())
parent = [ i for i in range(v+1) ]
edges = []

# 간선 정보 입력
for _ in range(e) :
    x, y, c = map(int, input().split())
    edges.append((c, x, y))
edges.sort() # 정렬

cost = 0
for edge in edges :
    c, x, y = edge
    if parent[x] != parent[y] :
        cost += c
        union(x, y)

print(cost)