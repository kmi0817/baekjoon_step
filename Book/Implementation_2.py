N, M = map(int, input().split())
x, y, d = map(int, input().split())

maps = []
for _ in range(N) :
    maps.append(list(map(int, input().split())))

print(maps)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

