import sys
input = sys.stdin.readline

def find_root(node) :
    if parent[node] != node :
        parent[node] = find_root(parent[node])
    return parent[node]

def union(a, b) :
    child = max(parent[a], parent[b])
    parent[child] = find_root(min(parent[a], parent[b]))

# v: 노드 개수 e: 간선 개수
v, e = map(int, input().split())

# 부모 리스트 생성 및 초기화
parent = [ i for i in range(v+1) ]

for _ in range(e) :
    a, b = map(int, input().split())
    union(a, b)

for n in range(1, v+1) :
    find_root(n)

# cycle check
Flag = True
for i in range(1, v) :
    if parent[i] != parent[i+1] :
        Flag = False
        break
if Flag :
    print("사이클이 발생했습니다.")
else :
    print("사이클이 없습니다.")