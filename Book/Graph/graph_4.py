from collections import deque
import copy
import sys
input = sys.stdin.readline

n = int(input())

hours = [0] * (n+1)
graph = [ [] for _ in range(n+1) ]
indegree = [0] * (n+1)

# 입력
for i in range(1, n+1) :
    data = list(map(int, input().split()))

    hours[i] = data[0]
    for node in data[1:-1] :
        indegree[i] += 1
        graph[node].append(i)

# 위상정렬
def topology_sort() :
    result = copy.deepcopy(hours)
    q = deque()

    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()

        for node in graph[now] :
            result[node] = max(result[node], result[now] + hours[node])
            indegree[node] -= 1
            if indegree[node] == 0 :
                q.append(node)

    # 출력
    for i in range(1, n+1) :
        print(result[i])

# 실행
topology_sort()