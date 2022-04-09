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
    if node != root :
        return find_root(root, parents[root])
    
    return node

# 부모 테이블 출력
print("부모 테이블:", end=" ")
for n in parents[1:] :
    print(n, end=" ")

print()

# 각 원소가 속한 집합
print("각 원소가 속한 집합:", end=" ")
for n in range(1, v+1) :
    print(find_root(n, parents[n]), end=" ")