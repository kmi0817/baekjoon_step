import sys
input = sys.stdin.readline

def find_root(node) :
    if parent[node] != node :
        parent[node] = find_root(parent[node])
    return parent[node]

n, m = map(int, input().split())
parent = [ i for i in range(n+1) ]

for _ in range(m) :
    oper, a, b = map(int, input().split())

    if oper == 0 :
        child = max(parent[a], parent[b])
        parent[child] = find_root(min(parent[a], parent[b]))
    else :
        if parent[a] == parent[b] :
            print("YES")
        else :
            print("NO")