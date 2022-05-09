from collections import deque

n = int(input())  # 모험가 수
chart = list(map(int, input().split()))  # 공포도

chart.sort()  # 오름차순 정렬
q = deque(chart)  # 큐

answer = 0
while q:
    value = q[0]  # 가장 낮은 공포도

    if len(q) >= value:
        print(q)
        print(f'value before popleft() : {value}')
        for i in range(value):
            q.popleft()
        print()
        print(f'value after popleft() : {value}')

        answer += 1
    else:
        break

print(answer)
