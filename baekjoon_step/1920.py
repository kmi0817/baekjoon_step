import sys
input = sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))
ns.sort()

m = int(input())
ms = list(map(int, input().split()))

for x in ms :
    start, end = 0, n - 1
    is_there = False
    while start <= end :
        i = (start + end) // 2
        if x == ns[i] :
            is_there = True
            break
        elif x < ns[i] :
            end = i - 1
        else :
            start = i + 1
        
    if is_there :
        print(1)
    else :
        print(0)
