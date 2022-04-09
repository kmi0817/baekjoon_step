import sys
input = sys.stdin.readline

# v: 노드 개수 e: 간선 개수
v, e = map(int, input().split())

parents = [ i for i in range(v+1) ]

# 간선 입력
for i in range(e) :
    a, b = map(int, input().split())

    child = max(a, b)
    parents[child] = min(parents[a], parents[b])

print(parents[1:])