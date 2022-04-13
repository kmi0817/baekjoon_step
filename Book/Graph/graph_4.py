import sys
input = sys.stdin.readline

n = int(input())

hours = [0] * (n+1)
graph = [ [] for _ in range(n+1) ]
indegree = [0] * (n+1)

# 입력
for i in range(n) :
    data = list(map(int, input().split()))

    hours[i] = data[0]
    for n in data[1:-1] :
        indegree[i] += 1
        graph[i].append(n)