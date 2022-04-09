# get Idea from the book

import sys
input = sys.stdin.readline

def find_parent(parent, node) :
    if parent[node] != node :
        return find_parent(parent, parent[node])
    return node

def union(parent, a, b) :
    child = max(parent[a], parent[b])

    parent[child] = find_parent(parent, min(parent[a], parent[b]))

# v: 노드 개수 e: 간선 개수
v, e = map(int, input().split())

parent = [ i for i in range(v+1) ]

for i in range(e) :
    a, b = map(int, input().split())
    union(parent, a, b)

# 각 원소가 속한 집합
print("각 원소가 속한 집합:", end=" ")
for i in range(1, v+1) :
    print(find_parent(parent, i), end=" ")
print()

# 부모 테이블 내용 출력
print("부모 테이블:", end=" ")
for n in parent[1:] :
    print(n, end=" ")