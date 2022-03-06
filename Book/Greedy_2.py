N, M = map(int, input().split())

_max = -1
for row in range(N) :
    m = list(map(int, input().split()))
    if _max < min(m) :
        _max = min(m)

print(_max)