import sys
input = sys.stdin.readline

# v: 노드 개수 e: 간선 개수
v, e = map(int, input().split())

parents = [ i for i in range(v+1) ]

# 간선 입력
for i in range(e) :
    a, b = map(int, input().split())

    child = max(parents[a], parents[b])
    parents[child] = min(parents[a], parents[b])

# 재귀함수
def find_root(node, root) :
    if node == root :
        return node
    
    find_root(root, parents[root])

for n in range(1, v+1) :
    parents[n] = find_root(n, parents[n])

print(parents[1:])