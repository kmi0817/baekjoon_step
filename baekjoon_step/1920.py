import sys
input = sys.stdin.readline # input()보다 빠른 sys.stdin.readline() 사용

# n
n = int(input())
ns = list(map(int, input().split()))
ns.sort() # 이진 탐색을 위한 오름차순 정렬

# m
m = int(input())
ms = list(map(int, input().split()))

for x in ms : # ms 리스트 내 모든 원소에 대해 이진 탐색 진행함
    start, end = 0, n - 1
    is_there = False # ns 리스트에 x 값이 존재하는지 표시하는 변수

    while start <= end :
        i = (start + end) // 2 # 중간 인덱스 설정

        if x == ns[i] :
            is_there = True
            break
        elif x < ns[i] : # x 값이 ns 중간값보다 작을 때
            end = i - 1
        else :
            start = i + 1 # x 값이 ns 중간값보다 클 때
        
    if is_there :
        print(1)
    else :
        print(0)
