import sys
input = sys.stdin.readline

def find_root(node) :
    if parent[node] != node :
        parent[node] = find_root(parent[node])
    return parent[node]

def union(a, b) :
    child = max(parent[a], parent[b])
    parent[child] = find_root(min(parent[a], parent[b]))

n, m = map(int, input().split())
parent = [ i for i in range(n+1) ]
edges = []

for _ in range(m) :
    a, b, d = map(int, input().split())
    edges.append((d, a, b))

edges.sort()

cost = []
for edge in edges :
    d, a, b = edge
    if parent[a] != parent[b] :
        union(a, b)
        cost.append(d)
    
print(sum(cost) - max(cost))
