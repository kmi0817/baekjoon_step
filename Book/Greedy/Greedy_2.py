N, M = map(int, input().split())

_max = -1
for row in range(N) :
    m = list(map(int, input().split()))

    _max = max(_max, min(m)) # find bigger mininum
    # if _max < min(m) :
        # _max = min(m)

print(_max)